Модели и формы

### Установка
1. Скопировать репозиторий
```bash
git clone https://github.com/username/lidiaakorovkinaa/django.study.git
```

2. Установить зависимости
```bash
pip install -r requirements.txt
```

3. Создать виртуальное окружение
```bash
cd blog
python3 -m venv venv
```

4. Перейти в папку с виртуальным окружением и запустить его
```bash
cd venv\Scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Activate.ps1
```
5. Выполнить миграции
```bash
python manage.py makemigrations otzivi
python manage.py migrate
```
6. Создать учетную запись админа
```bash
python manage.py createsuperuser
```

7. Запустить сервер:
```bash
python3 manage.py runserver
```

8. Открыть в браузере
```bash
 http://127.0.0.1:8000/
```

9. Перейти на страницу с отзывами и оставить отзыв
```bash
http://127.0.0.1:8000/otzivi/
```

10. Для публикации отзыва перейти в режим админа
```bash
http://127.0.0.1:8000/admin/
```

11. В разделе с отзывами поставить галочку напротив отзыва и сохранить. Отзыв появится на странице

## Версия Python
Python 3.15.0a3

## Автор
Коровкина Лидия 2-МГЗ-2

