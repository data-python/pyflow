import json

def convert_json_to_csv(jsonPath):
    try:
        with open(jsonPath, 'r', encoding='gbk') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])

        # 数据
        for obj in data:
            output += f'\n'
            for item in obj:
                output += f'{obj[item]},'

        with open(jsonPath + ".csv", 'w', encoding='gbk') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')

    return jsonPath + ".csv"