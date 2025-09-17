import redis
import time


myredis = redis.Redis(host="myredis", port=6379, decode_responses=True)


while True:
    try:
        myredis.ping()
        print("Connected")
        break
    except redis.exceptions.ConnectionError:
        print("Waiting..")
        time.sleep(1)

print("Writing data..")
myredis.set("message", "Hello World!")
myredis.set("user:1", "Alice")
myredis.lpush("tasks", "task1", "task2", "task3")  # push items into a list

print("Reading data..")
msg = myredis.get("message")
user1 = myredis.get("user:1")
tasks = myredis.lrange("tasks", 0, -1)  # get all list items

print("Message:", msg)
print("User 1:", user1)
print("Tasks:", tasks)
