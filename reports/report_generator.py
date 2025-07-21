from datetime import datetime

def generate_report(data):
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("?? Matrix Report\n\n")
        f.write(data)
