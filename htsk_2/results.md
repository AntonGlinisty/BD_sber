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

## Развернем кластер redis в docker контейнерах

#### Поднятие контейнеров:

```
docker compose up -d
```

#### Связь нод друг с другом

```
docker exec -it node1 redis-cli --cluster create \
 node1:7000 node2:7001 node3:7002 --cluster-replicas 0
```

#### Проверка статуса redis кластера

```
docker exec -it node1 redis-cli --cluster check node1:7000
```

#### Результаты:

<image src="./screenshots/cluster.png">