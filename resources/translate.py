import csv
import json

if __name__ == "__main__":
    data = {}
    with open('french.csv', 'r') as csv_f:
        reader = csv.DictReader(csv_f)
        for row in reader:
            class_name = row.pop('class')
            data_points = row['dataPoints']
            if len(data_points):
                row['dataPoints'] = data_points.split('##')
            data[class_name] = row

    data_json = json.dumps(data)
    js = "let frenchTranslationData = " + data_json

    with open("french_translation.js", "w") as f:
        f.write(js)
