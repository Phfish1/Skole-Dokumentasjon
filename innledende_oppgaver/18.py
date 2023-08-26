def file_to_dict(filename):

    file = open(filename, "r")
    file_lines = file.readlines()

    file_dictionary = {}
    for i in range(0, len(file_lines)):
        curent_line = file_lines[i].split()
        curent_name = curent_line[0]
        curent_number = int(curent_line[1])

        file_dictionary[curent_name] = curent_number

    return file_dictionary

def best_salesmen(sales_dict):
    
    ### Extracts the best "sales men" and appends them to {current_best_list}
    current_best_list = [["", 0]]
    for key in sales_dict:
        current_sales = sales_dict[key]
        current_salesman = key

        if current_sales >= current_best_list[0][1]:
            if current_sales != current_best_list[0][1]:
                current_best_list[0] = [current_salesman, current_sales]
            else:
                current_best_list.append([current_salesman, current_sales])

    ### Checks if more than 1 "best salesman"
    if len(current_best_list) > 1:
        best_salesmen_string = ""
        for i in range(0, len(current_best_list)):
            if i + 1 != len(current_best_list):
                best_salesmen_string += f"{current_best_list[i][0]} with {current_best_list[i][1]} sales & "
            else:
                best_salesmen_string += f"{current_best_list[i][0]} with {current_best_list[i][1]} sales"

        return best_salesmen_string ### TO TEST THIS, UNCOMMENT {file = "innledende_oppgaver/sandbox/salesnumbers2.txt"} IN THE INITIALIZER CODE
    else:
        return f"{current_best_list[0][0]} {current_best_list[0][1]}"

def total_sales(sales_dict):
    sales_sum = 0
    for key in sales_dict:
        current_sale = sales_dict[key]
        sales_sum += current_sale

    return sales_sum

def average_sales(sales_dict):
    sales_sum = total_sales(sales_dict)
    average = sales_sum / len(sales_dict)

    return average

def main(file):
    try:
        company_sales_dictionary = file_to_dict(file)
        company_best_salesmen = best_salesmen(company_sales_dictionary)
        company_total_sales = total_sales(company_sales_dictionary)
        company_average_sales = average_sales(company_sales_dictionary)

        string_output = ""
        string_output += f"Months best sales are: {company_best_salesmen}\n"
        string_output += f"Active salesmen this month: {len(company_sales_dictionary)}, A total of {company_average_sales} sales!\n"
        string_output += f"Average sales where: {company_total_sales} per salesman"

        return string_output
    except Exception as error:
        print("<! Is the file specified correct?, Rember to remove all white space !>")
        raise error

### Initializer code
file = "innledende_oppgaver/sandbox/salesnumbers.txt"
#UNCOMMENT TO TEST "multiple best_salesmen"
#file = "innledende_oppgaver/sandbox/salesnumbers2.txt"
result = main(file)

print(result)