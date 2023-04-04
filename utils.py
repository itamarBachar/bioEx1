def check_input(input_text):
    for i in input_text:
        # cast the input to float and check if it is a number\
        try:
            float(i)
        except ValueError:
            return False
    # check if the first input is a number and is not between 0 and 1
    if float(input_text[0]) < 0 or float(input_text[0]) > 1:
        return False
    # go over for 2 to 5 and check if there sum is 1
    if sum([float(input_text[i]) for i in range(2, 6)]) != 1:
        return False
    return True
