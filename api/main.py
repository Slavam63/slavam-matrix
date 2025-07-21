from scripts.faq_importer import import_faq
from utils.ai_adapt import adapt_faq
from reports.report_generator import generate_report
from notifier import notify_result
from utils.log_handler import write_daily_log, reset_log_monthly

def run_pipeline():
    print("🚀 Старт пайплайна: FAQ → адаптация → отчёт → лог")

    # Импорт FAQ
    faq_items = import_faq()
    if not faq_items:
        print("⚠️ Вопросов нет — процесс прерван.")
        write_daily_log("⛔ Вопросы не найдены — запуск остановлен.")
        return

    # Адаптация
    adapted = adapt_faq(faq_items)

    # Генерация отчета
    report_text = "\n".join([f"Q: {q}\nA: {a}" for q, a in adapted])
    generate_report(report_text)

    # Запись лога
    write_daily_log(f"✅ Обработано {len(faq_items)} FAQ-вопросов")
    reset_log_monthly()

    # Уведомление (опционально)
    # notify_result()

    print("📘 Цикл завершён — отчёт создан, лог записан.")
