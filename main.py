# Импорт библиотек
from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}  # Храним пользователей в виде словаря


@app.get('/users')
async def get_users() -> dict:
    # Возвращаем список всех пользователей
    return users


@app.post('/user/{username}/{age}')
async def registered_user(username: str, age: int) -> str:
    # Регистрируем нового пользователя с уникальным ID
    current_id = str(int(max(users, key=int)) + 1)
    users[current_id] = f'Имя: {username}, возраст: {age}'
    return f'User {current_id} is registered!'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    # Обновляем данные существующего пользователя
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated!'


@app.delete('/user/{user_id}')
async def deleted_user(user_id: str) -> str:
    # Удаляем пользователя по его ID
    users.pop(user_id)
    return f'The user {user_id} is deleted'
