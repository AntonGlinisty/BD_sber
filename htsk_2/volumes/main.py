import json
import redis
import time

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

with open("data.json", "r", encoding="utf-8") as file:
   data = json.load(file)

create_time = []
select_time = []
data_structures = ["string", "hset", "zset", "list"]

def Create():
    # String
   
    start_time = time.time()

    redis_client.set("data_string", str(data))

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

    # Hset

    start_time = time.time()

    redis_client.hset("data_hset", mapping={
        "data" : str(data)
    })

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

    # Zset

    start_time = time.time()

    redis_client.zadd("data_zset", mapping={
        str(data) : 1
    })

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

    # List

    start_time = time.time()

    redis_client.lpush("data_list", str(data))

    end_time = time.time()
    create_time.append((end_time - start_time) * 1000)

def Select():
    # String
    
    start_time = time.time()

    redis_client.get("data_string")

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

    # Hset

    start_time = time.time()

    redis_client.hgetall("data_hset")

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

    # Zset

    start_time = time.time()

    redis_client.zrange("data_zset", 0, -1)

    end_time = time.time()
    select_time.append((end_time - start_time) * 1000)

    # List

    start_time = time.time()

    redis_client.lrange("data_list", 0, -1)

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

redis_client.close()