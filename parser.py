import csv

def get_words_list(file_path, just_important):
    file = open(file_path)
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        rows.append(row)
    
    result = []
    for item in rows:
        importance = True if not item[1].strip() == '' else False
        if not just_important:
            result.append({
                "word":item[0],
                "meaning":item[1],
                "example":item[2],
            })
        elif just_important and importance:
            result.append({
                "word":item[0],
                "meaning":item[1],
                "example":item[2],
            })
    file.close()
    return result

if __name__ == "__main__":
   list = get_words_list("review-files-csv/example.csv", True)
   print(list)
