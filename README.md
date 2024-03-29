# Описание проекта:

Django проект, позволяющий взаимодействовать с БД
при помощи API (DRF)

## Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Ogyrecheg/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -3.7 -m venv venv
```

```
source venv/Scripts/activate
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


**Технологии:**
- Python
- Django
- SQlite
- DRF
- GitHub

### Автор проекта:
студент когорты №17 [Шевченко Александр](https://github.com/Ogyrecheg)
