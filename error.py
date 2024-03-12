import json, csv, re
jsonpath = 'logs.json'

try:
    with open(jsonpath) as file1:
        data = json.load(file1)
        with open('logs.csv','w',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=data[0].keys())
            writer.writeheader()
            pattern = r"ERROR"
            for log in data:
                match = re.search(pattern,log['level'],re.IGNORECASE)
                if match:
                    writer.writerow(log)
except FileNotFoundError:
    print('json file not found!')
except Exception as e:
    print(f'Error: {e} ')

