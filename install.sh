#!/bin/bash

echo "🚀 Установка Матрицы начинается..."

# 🐳 Установка Docker (если отсутствует)
if ! command -v docker &> /dev/null; then
  echo "⚙️ Устанавливаю Docker..."
  apt-get update
  apt-get install -y docker.io
fi

# 🧬 Сборка образа
echo "🔧 Собираем Docker-образ..."
docker build -t slavam-matrix .

# 🛞 Запуск контейнера
echo "🖥️ Запускаем контейнер..."
docker run -d -p 8000:8000 --name matrix_app slavam-matrix

echo "✅ Матрица активирована на порту 8000"
echo "🌐 Перейти: http://<IP_твоей_виртуальной_машины>:8000"
