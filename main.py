import datetime
import pytz
from typing import Union

from fastapi import FastAPI

app = FastAPI()

def count_primes_up_to_n(n: int) -> int:
    if n < 2:
        return 0
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return sum(primes)

@app.get("/primes/{n}")
def get_prime_count(n: int):
    return {"prime_count": count_primes_up_to_n(n)}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/day")
def get_day():
    day_of_week = datetime.datetime.now().strftime("%A")
    return {"day": day_of_week}

@app.get("/day-of-month")
def get_day_of_month():
    day_of_month = datetime.datetime.now().day
    return {"day_of_month": day_of_month}

@app.get("/current-time")
def get_current_time():
    eastern = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(eastern)
    formatted_time = now.strftime("The current time is %I:%M %p EST on %A %B %d, %Y")
    return {"current_time": formatted_time}

def check_birthday() -> str:
    today = datetime.datetime.now()
    if today.month == 8 and today.day == 1:
        return "Happy Birthday!"
    else:
        return "Today is not your birthday."

@app.get("/birthday")
def get_birthday_message():
    return {"message": check_birthday()}