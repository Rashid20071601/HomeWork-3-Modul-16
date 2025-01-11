# Импорт библиотек
from fastapi import FastAPI, HTTPException, Path
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


async def update_user(
    user_id: str,
    username: str,
    age: Annotated[int, Path(gt=0)]
) -> str:
    # Проверяем, существует ли пользователь с указанным ID
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    # Обновляем данные существующего пользователя
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated!'


async def deleted_user(user_id: str) -> str:
    # Проверяем, существует ли пользователь с указанным ID
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    # Удаляем пользователя по его ID
    users.pop(user_id)
    return f'The user {user_id} is deleted!'
