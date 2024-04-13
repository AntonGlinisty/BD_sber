##### Скачиваем couchdb по официальной инструкции: <https://docs.couchdb.org/en/latest/install/unix.html#installation-using-the-apache-couchdb-convenience-binary-packages>

##### Проверим, что служба couchdb активна:
```
sudo systemctl status couchdb
```

<image src="./screenshots/daemon.png">

##### Создадим базу и документ с помощью couchdb python API:
```
python3 main.py
```

##### Или же воспользуемся couchdb web interface. Введем http://127.0.0.1:5984/_utils в поисковой строке браузера.

##### Создадим базу:

<image src="./screenshots/create_db.png">

##### Создадим документ:

<image src="./screenshots/create_doc.png">

##### Прописываем в html файле путь к инсталяции couchdb, запускаем его и нажимаем кнопку "sync".

<image src="./screenshots/html.png">

##### Остановим службу couchdb и убедимся в том, что фамилия все еще отображается:

```
sudo systemctl stop couchdb
```