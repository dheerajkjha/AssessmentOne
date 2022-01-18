# Remove all spaces
def func_format_input(user_input_string):
    formatted_input_string = user_input_string.replace(' ', '')
    formatted_input_string = formatted_input_string.replace('.', '')
    formatted_input_string = formatted_input_string.replace(',', '')
    formatted_input_string = formatted_input_string.lower()
    return formatted_input_string


def func_is_palindrome(formatted_input_string):
    func_format_input(formatted_input_string)
    reversed_input_string = ''
    for letter in formatted_input_string:
        reversed_input_string = letter + reversed_input_string
    if reversed_input_string == formatted_input_string:
        print(True)
    else:
        print(False)


user_input = input('Please enter a string: ')
func_is_palindrome(func_format_input(user_input))
