# Анализ Покупок в Супермаркете 

Интерактивное веб-приложение для анализа данных о покупках в супермаркете, созданное с помощью Streamlit.

**Демо:** [https://supermarketpurchaseanalysis.streamlit.app/](https://supermarketpurchaseanalysis.streamlit.app/)

[English version](README.md)

## Возможности

- Интерактивная визуализация паттернов покупок и трендов
- Фильтрация по категориям товаров, способам оплаты и типам клиентов
- Аналитика продаж и анализ выручки
- Анализ распределения способов оплаты
- Современный и адаптивный интерфейс

## Быстрый старт

### Локальная установка

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/supermarket-analysis.git
cd supermarket-analysis

# Установите зависимости
pip install -r requirements.txt

# Сгенерируйте тестовые данные
python generate_data.py

# Запустите приложение
streamlit run app.py
```

### Docker

```bash
# Соберите образ
docker build -t supermarket-analysis .

# Запустите контейнер
docker run -p 8501:8501 supermarket-analysis
```

Откройте браузер по адресу `http://localhost:8501`

## Структура проекта

```
.
├── app.py                     # Основное Streamlit приложение
├── generate_data.py           # Генератор тестовых данных
├── supermarket_data.xlsx      # Файл с данными
├── requirements.txt           # Зависимости Python
├── Dockerfile                 # Docker configuration
└── .streamlit/
    └── config.toml            # Настройки Streamlit
```

## Технологии

- **Python 3.11+**
- **Streamlit** - Веб-интерфейс
- **Pandas** - Обработка данных
- **Plotly** - Интерактивные графики
- **OpenPyXL** - Работа с Excel файлами

## Лицензия

Лицензия MIT - подробности в файле [LICENSE](LICENSE).

## Участие в разработке

Приветствуются любые предложения! Открывайте issues или отправляйте pull requests.
