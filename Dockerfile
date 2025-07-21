# 🐍 Базовый образ Python
FROM python:3.11-slim

# 📂 Рабочая директория внутри контейнера
WORKDIR /app

# 📦 Копируем всю структуру Матрицы внутрь
COPY SlavamMatrix/ ./SlavamMatrix/
WORKDIR /app/SlavamMatrix

# 📜 Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 🌐 Открываем порт для API
EXPOSE 8000

# 🚀 Команда запуска Матрицы
CMD ["uvicorn", "api.main:run_pipeline", "--host", "0.0.0.0", "--port", "8000"]
