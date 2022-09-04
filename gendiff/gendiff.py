import json


def generate_diff(path_1, path_2):
    file_1 = json.load(open(path_1))
    file_2 = json.load(open(path_2))
    file_1_keys = [key for key in file_1.keys()]
    file_2_keys = [key for key in file_2.keys()]
    file_1_keys.extend(file_2_keys)
    all_keys = sorted(set(file_1_keys))
    result = '{'
    for key in all_keys:
        result += '\n'
        if key in file_1 and key in file_2:
            if file_1[key] == file_2[key]:
                result += f'  {key}: {file_1[key]}'
            else:
                result += f'- {key}: {file_1[key]}\n+ {key}: {file_2[key]}'
        elif key not in file_1:
            result += f'+ {key}: {file_2[key]}'
        elif key not in file_2:
            result += f'- {key}: {file_1[key]}'
    return result + '\n}'
