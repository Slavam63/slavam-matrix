import os
from datetime import datetime
from calendar import monthrange

def write_daily_log(entry: str, path="log/report_log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {entry}\n")

def reset_log_monthly(path="log/report_log.txt"):
    now = datetime.now()
    last_day = monthrange(now.year, now.month)[1]
    if now.day == last_day:
        archive_dir = "log/archive"
        os.makedirs(archive_dir, exist_ok=True)
        archive_path = os.path.join(archive_dir, f"report_log_{now.strftime('%Y_%m')}.txt")
        if os.path.exists(path):
            os.replace(path, archive_path)
            print(f"🧾 Лог за {now.strftime('%Y.%m')} перенесён в архив.")
