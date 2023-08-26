def homemade_slicer(main_string, slice_start, slice_end):

    sliced_string = ""
    for i in range(0, len(main_string)):
        if i >= slice_start and i < slice_end:
            sliced_string += main_string[i]

    return sliced_string

print(homemade_slicer("Hello man", 0, 5))