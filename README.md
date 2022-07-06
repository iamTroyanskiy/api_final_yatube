[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

<h1 align="center">
  <br>
  <img src="https://github.com/tonik350/img/blob/main/API.png?raw=true"  width="500"></a>
  <br>
    API для социальни сети Yatube
  <br>
</h1>

# Описание
API для взаимодействия с социальной сетью Yatube.

## Технологии

* Python v3.7
* Django v2.2.16
* djangorestframework v3.12.4
* djangorestframework-simplejwt v4.7.2
* PyJWT v2.1.0
* redoc

# Установка
1. Склонировать репозиторий и перейти в папку с проектом командами :
 ```
 git clone git@github.com:Jloogle/api_final_yatube.git
 ```
2. Установить виртуальное окружение и активировать его:
```
 python3 -m venv venv
 ```
 ```
 source venv/bin/activate
 ```
3. Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python3 manage.py migrate
```
5. Запустить сервер командой
```
python3 manage.py runserver
```

# Примеры запросов к API

- `api/v1/api-token-auth/` (POST): передать логин и пароль, получить токен.

- `api/v1/posts/` (GET, POST): получить список всех постов или 🔐создать новый пост.

- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получить, 🔐редактировать или 🔐удалить пост по id.

- `api/v1/posts/{post_id}/comments/` (GET, POST): получить список всех комментариев поста с id=post_id или 🔐создать новый, указав id поста, который нужно прокомментировать.

- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получить, 🔐редактировать или 🔐удалить комментарий по id у поста с id=post_id.

- `api/v1/groups/` (GET): получить список всех групп.

- `api/v1/groups/{group_id}/` (GET): получить информацию о группе по id.

- `api/v1/follow/` (GET, POST): 🔐Возвращает все подписки пользователя, сделавшего запрос.

- `api/v1/jwt/create/` (POST): Получение JWT-токена.

- `api/v1/jwt/refresh/` (POST): Обновление JWT-токена.

- `api/v1/jwt/verify/` (POST): Проверка JWT-токена.
```
🔐 --> Доступно только для авторизованных пользователей.
```
