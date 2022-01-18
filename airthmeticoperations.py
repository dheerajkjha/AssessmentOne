input_string = input("Please enter a String: ")

input_string = input_string.strip(' equals')
# print(input_string)

operator_list = ['plus', 'minus', 'times', 'divided by']
operator_sign = ['+', '-', '*', '/']
operator_sign_index = 0

for operator in operator_list:
    input_string = input_string.replace(operator, operator_sign[operator_sign_index])
    operator_sign_index += 1

# print(input_string)
calculated_value = eval(input_string)
print(int(calculated_value))

