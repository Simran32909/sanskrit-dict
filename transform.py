import json

def convert_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        line = line.strip()
        if line:
            key_value = line.split(':')
            if len(key_value) == 2:
                word = key_value[0].strip().strip('"')
                meaning = key_value[1].strip().strip('"')
                data[word] = meaning

    json_data = json.dumps(data, ensure_ascii=False, indent=4)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

input_f = 'dic-3.txt'
output_f= 'dic-3.json'
convert_json(input_f, output_f)