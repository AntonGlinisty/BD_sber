from rediscluster import RedisCluster
import json
import time

nodes = [
    {"host": "127.0.0.1", "port": "7000"},
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"}
]

redis_cluster = RedisCluster(startup_nodes=nodes, decode_responses=True)

with open("data.json", "r", encoding="utf-8") as file:
   data = json.load(file)

create_time = []
select_time = []
data_structures = ["string", "hset", "zset", "list"]

def Create():
    # String
   
    start_time = time.time()

    redis_cluster.set("data_string", str(data))

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

    # Hset

    start_time = time.time()

    redis_cluster.hset("data_hset", mapping={
        "data" : str(data)
    })

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

    # Zset

    start_time = time.time()

    redis_cluster.zadd("data_zset", mapping={
        str(data) : 1
    })

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

    # List

    start_time = time.time()

    redis_cluster.lpush("data_list", str(data))

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

def Select():
    # String
    
    start_time = time.time()

    redis_cluster.get("data_string")

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

    # Hset

    start_time = time.time()

    redis_cluster.hgetall("data_hset")

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

    # Zset

    start_time = time.time()

    redis_cluster.zrange("data_zset", 0, -1)

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

    # List

    start_time = time.time()

    redis_cluster.lrange("data_list", 0, -1)

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

Create()
Select()

print("Create time in milliseconds:")
for i in range(len(data_structures)):
   print(data_structures[i], create_time[i])

print("\nSelect time in milliseconds:")
for i in range(len(data_structures)):
   print(data_structures[i], select_time[i])

redis_cluster.close()