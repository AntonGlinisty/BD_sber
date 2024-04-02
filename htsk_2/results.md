## Развернем redis в docker контейнере

#### Создание образа:

```
docker build -t redis .
```

#### Запуск контейнера:

```
docker run -w /volumes --name redis -d redis
```

#### Заходим в контейнер для выполнения скрипта:

```
docker exec -it redis bash
```

#### Запуск скрипта:

```
python3 main.py
```

#### Результаты:

<image src="./screenshots/time.png">