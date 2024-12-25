# Импорт библиотек
from fastapi import FastAPI, Path
from typing import Annotated

# Инициализация приложения
app = FastAPI()

# База данных сообщений
messages_db = {'0': 'Первый пост в FastAPI'}

# Получение всех сообщений
@app.get('/')
async def get_all_messages() -> dict:
    return messages_db

# Получение сообщения по ID
@app.get('/message/{message_id}')
async def get_message(message_id: str) -> dict:
    return messages_db[message_id]

# Создание нового сообщения
@app.post('/message')
async def create_message(message: str) -> str:
    current_index = str(int(max(messages_db, key=int)) + 1)
    messages_db[current_index] = message
    return 'Сообщение создано!'

# Обновление сообщения
@app.put('/message/{message_id}')
async def update_message(message_id: str, message: str) -> str:
    messages_db[message_id] = message
    return 'Сообщение обновлено!'

# Удаление сообщения по ID
@app.delete('/message/{message_id}')
async def delete_message(message_id: str) -> str:
    messages_db.pop(message_id)
    return f'Сообщение с ID {message_id} удалено!'

# Удаление всех сообщений
@app.delete('/')
async def delete_all_messages() -> str:
    messages_db.clear()
    return 'Все сообщения удалены!'
