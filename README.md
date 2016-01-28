1. Установить необходимые библиотеки из requiremenets.txt
2. Запустить из папки REDIS, redis-server.exe.
3. Из под окружения python, в командной строке прописать:
  3.1  "start python manage.py runserver" + Enter - запустит сервер
  3.2  "start python manage.py celeryd" + Enter - запустит воркер celery
4. В браузере набрать 127.0.0.1:8000