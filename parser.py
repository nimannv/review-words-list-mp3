import csv

def get_words_list(file_path):
    file = open(file_path)
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        rows.append(row)
    
    result = []
    for item in rows:
        result.append({
            "word":item[0],
            "important": True if not item[1].strip() == '' else False,
            "description":item[2],
        })
    file.close()
    return result
