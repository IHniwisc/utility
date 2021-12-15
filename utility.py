
import json


def replace_string(data_list, target, replaced):
    result = []
    for i in data_list:
        buffer = i.replace(target, replaced)
        result.append(buffer)
    return result


def remove_string(data_list, target):
    result = []
    for i in data_list:
        if not target in i:
            result.append(i)
    return result


def keep_string(data_list, target):
    result = []
    for i in data_list:
        if target in i:
            result.append(i)
    return result


def import_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def export_json(export_file_name, data):
    with open(export_file_name, 'w') as file:
        json.dump(data, file)


def save_as_log(export_file_path, data):
    with open(export_file_path, mode='w') as file:
        for i in data:
            file.write(i+"\n")