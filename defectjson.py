import json

with open("defects-export-0-100.json", 'r') as json_file:
    json_data = json_file.read()

    json_object = json.loads(json_data)

    creation_time_field = 5
    creation_time_field_value = 0

    defect_id_field = 6
    defect_id_field_value = 0

    for defect_number in range(len(json_object['entities'])):
        defect_creation_time = json_object['entities'][defect_number]['Fields'][creation_time_field]['values'][creation_time_field_value]['value']
        if '2016-09-01' <= defect_creation_time <= '2016-09-30':
            defect_id = json_object['entities'][defect_number]['Fields'][defect_id_field]['values'][defect_id_field_value]['value']
            print('Defect ID: {}'.format(defect_id))
