import json

with open("Nested-JSON-1.json", 'r') as json_file:

    json_data = json_file.read()

    json_object = json.loads(json_data)

    output_names = ''

    for object_number in range(len(json_object)):
        for topping_number in range(len(json_object[object_number]['topping'])):
            if json_object[object_number]['topping'][topping_number]['type'] == 'Glazed':
                output_names += json_object[object_number]['name'] + ', '

    if output_names != '':
        final_output_names = output_names[:-2]
        print('"{}"'.format(final_output_names))
    else:
        print('"No matches found"')

