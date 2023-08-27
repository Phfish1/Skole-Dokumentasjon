def main():
    imported_file = __import__("19") ### Had to do it this way because of "numbered" naming scheme ;(
    my_bike = imported_file.Motorcycle("Toyota", 12345, 8005)
    my_brothers_bike = imported_file.Motorcycle("Sosse_merke", 9547189571985, 9)

    my_bike.drive(10)
    print(my_bike.get_status())

    my_brothers_bike.drive(1)
    print("\n", my_brothers_bike.get_status())

main()
