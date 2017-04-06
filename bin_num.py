def num_convert(bin_num):
    """Converts the list of ints to a string splits into
    individual elements, and reverses the elements
    """
    bin_num = str(bin_num)
    bin_list = list(bin_num)
    bin_list.reverse()
    return bin_list
    
def compute_power(bin_num):
    """Calculates the value of the binary digit
    """
    bin_list = num_convert(bin_num)
    int_list = []
    for char in bin_list:
        int_list.append(int(char))
        
    result_list = 0
    i = 0
    while i < len(int_list):
        if int_list[i] == 1:
            result = 2 ** int(i)
            result_list += result
        elif int_list[i] == 0:
            result_list += 0
        i += 1
    return result_list

def error_msg(bin_num):
    """Determines whether the user input is valid, and
    returns an error message if the input is invalid
    """
    is_digit = bin_num.isdigit()
    is_error_0 = bin_num.find('0')
    is_error_1 = bin_num.find('1')
    if is_error_0 != -1 or is_error_1 != -1:
        decimal_num = compute_power(bin_num)
        print(decimal_num)
        main()
    elif is_error_0 == -1 and is_error_1 == -1 or is_digit is False:
        print('')
        print('************************ERROR************************')
        print('Binary numbers can only consist of 0\'s and/or 1\'s')
        print('Please enter a valid binary number or enter q to quit')
        print('*****************************************************')
        print('')
        main()

def continue_quit(bin_num):
    """Determines whether the user wants to quit the program
    """
    if bin_num == 'q' or bin_num =='Q':
        print('')
        print("Goodbye!")
    else:
        error_msg(bin_num)

def main():
    """Prompts the user to enter a binary number
    """
    print('')
    print('(Quit = q)')
    print('_____________________________________________')
    bin_num = input('Enter binary number: ')
    continue_quit(bin_num)
    

main()


# numbers which have a 0 or 1 in them, but also other numbers/letters
# do not throw the error message!