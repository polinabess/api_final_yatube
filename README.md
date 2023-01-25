# Проект «REST API для Yatube»

Данный проект является программным интерфейсом для социальной сети Yatube.

## Список технологий
* Python 3.7
* Django Rest Framework 3.2
* Simple-JWT
* SQLite3
* pytest

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/polinabess/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов и ответов API
#### 1
**GET** запрос
```
http://127.0.0.1:8000/api/v1/posts/
```
Ответ API
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
____
#### 2
**POST** запрос
```
http://127.0.0.1:8000/api/v1/posts/
```
Ответ API
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
___
#### 3
**PUT** запрос
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Ответ API
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
___
#### 4
**PATCH** запрос
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Ответ API
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
___
#### 5
**DELETE** запрос
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Ответ API
```
{
  "detail": "Учетные данные не были предоставлены."
}
```
___

Более подробно можно ознакомиться с запросами, после установки и запуска проекта по ссылке http://127.0.0.1:8000/redoc/

## License

[MIT](https://choosealicense.com/licenses/mit/)