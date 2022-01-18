output_string = ''
with open('Odd-Numbers.txt', 'r') as input_file:
    for line in input_file:
        new_line = line.rstrip('\n')
        if new_line.isdigit() and int(new_line) % 2 != 0:
            output_string += new_line + '\n'


with open('Odd-Numbers-output.txt', 'w') as output_file:
    output_file.write(output_string)
