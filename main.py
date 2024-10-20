from fastapi import FastAPI
import requests

app = FastAPI()


# Прописать эндпоинты
# 1. Домашняя страница. Открывается форма для внесения данных и загрузки excel файла
@app.get("/")
def root():
    pass


# 2. Эндпоинт для кнопки "Выгрузить". Отправка данных текущего документа в бд
@app.post("/load")
def load():
    pass


# 3. Для страницы проверки
@app.get("/check")
def check():
    pass


# 4. Для отправки документов в iiko
@app.get("/send")
def send():
    pass


# 5. Отображение страницы с результатом
@app.get("/result")
def result():
    pass


# 6. Отображение панели администратора
@app.get("/adminka")
def adminka():
    pass


# 7. Сохранение изменений на панели админа
@app.post("/save_config")
def save_config():
    pass


# 8. Синхронизация. Запрашивает данные с сервера iiko исходя из конфига
@app.get("/synchro")
def synchro():
    pass
