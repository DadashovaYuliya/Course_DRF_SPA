# SAP-приложение

## Описание:

Трекер полезных привычек на основе книги «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.

## Настройка сервера:

1. Подключитесь к своему серверу:
```
ssh user_name@your_server_ip
```
2. Запустите обновления:
```
sudo apt update
sudo apt upgrade
```
3. Настройте брандмауэр и откройте необходимые порты:
```
sudo ufw status
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
```

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:DadashovaYuliya/Course_DRF_SPA.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Настройте файл .env:
```
cd course_drf_spa/
nano .env

Для работы с django укажите Ваш секретный ключ и статус debug
SECRET_KEY=
DEBUG=

Для проекта используется база данных PostgreSQL. Укажите ваши параметры, предварительно создав пустую БД
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=

Для интеграции с телеграмм-ботом укажите токен
TELEGRAM_TOKEN=
```

4. Запустите контейнер:
```
docker-compose up
```
5. Автоматизация с CI/CD через GitHub Actions
```
Для автоматизации сборки, тестирования и деплоя проекта используется GitHub Actions.
Создайте новый репозиторий и добавьте все необходимые переменные среды в secrets.
Основные возможности:
1. Автоматическая проверка кода при каждом пуше или pull request.
2. Запуск тестов для обеспечения качества.
3. Автоматический деплой на сервер после успешных проверок.
```

## Приложения

1. Приложение habits, в котором описана модель Habit. 


## Контроллеры

1. Для модели Habit создан контроллер на основе viewsets с сериализатором HabitSerializer, контроллер на основе generics с сериализатором PublicHabitSerializer


## Маршрутизация:

1. Для представлений Habit настроена соответствующая маршрутизация.

## Тестирование:

1. Покрытие тестами:
Name                                                           Stmts   Miss  Cover
----------------------------------------------------------------------------------
config\__init__.py                                                 2      0   100%
config\asgi.py                                                     4      4     0%
config\celery.py                                                   6      0   100%
config\settings.py                                                37      0   100%
config\urls.py                                                     7      0   100%
config\wsgi.py                                                     4      4     0%
habits\__init__.py                                                 0      0   100%
habits\admin.py                                                    1      0   100%
habits\apps.py                                                     4      0   100%
habits\migrations\0001_initial.py                                  6      0   100%
habits\migrations\0002_initial.py                                  7      0   100%
habits\migrations\0003_alter_habit_is_pleasant_habit.py            4      0   100%
habits\migrations\__init__.py                                      0      0   100%
habits\models.py                                                  18      1    94%
habits\paginators.py                                               5      0   100%
habits\serializers.py                                             23      1    96%
habits\services.py                                                 5      5     0%
habits\tasks.py                                                   10     10     0%
habits\tests.py                                                   41      0   100%
habits\urls.py                                                     8      0   100%
habits\validators.py                                              19     10    47%
habits\views.py                                                   23      1    96%
manage.py                                                         11      2    82%
users\__init__.py                                                  0      0   100%
users\admin.py                                                     1      0   100%
users\apps.py                                                      4      0   100%
users\migrations\0001_initial.py                                   7      0   100%
users\migrations\0002_remove_user_tg_nick_user_tg_chat_id.py       4      0   100%
users\migrations\__init__.py                                       0      0   100%
users\models.py                                                   13      1    92%
users\permissions.py                                               4      0   100%
users\serializers.py                                               6      0   100%
users\tests.py                                                     1      0   100%
users\urls.py                                                      7      0   100%
users\views.py                                                    10      3    70%
----------------------------------------------------------------------------------
TOTAL                                                            302     42    86%
