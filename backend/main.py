from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psycopg2
 
app = FastAPI()

def connect():
    try:
        # пытаемся подключиться к базе данных
        print('RUN')
        conn = psycopg2.connect(dbname='memdb', user='back', password='passwordqwerty', host='localhost')
        cursor = conn.cursor()
        #  Получаем список всех пользователей
        cursor.execute('SELECT * FROM cars;')
        all_users = cursor.fetchall()

        for row in all_users:
            print(row)

        cursor.close() # закрываем курсор
        conn.close() # закрываем соединение

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')    
 
@app.get("/")
def read_root():
    html_content = "<h2>Hello World!</h2>"
    connect()
    return HTMLResponse(content=html_content)


