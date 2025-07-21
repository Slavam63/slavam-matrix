import csv

def import_faq(path="data/faq.csv"):
    faq_items = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                if len(row) == 2:
                    faq_items.append((row[0], row[1]))
    except FileNotFoundError:
        print("❌ Файл FAQ не найден:", path)
    return faq_items
