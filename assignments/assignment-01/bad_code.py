import sys
import os
import hashlib
import pickle
import subprocess
from typing import List

from db_helpers import run_query


def calculate_total(prices: List[float]) -> int:
    x = 0.0
    for p in prices:
        x += p
    return x


def calculate_total_with_tax(prices: List[float]) -> float:
    x = 0.0
    for p in prices:
        x += p
    return x * 1.13


def getUserOrders(username):
    return run_query("orders", username)


def hash_password(password):
    print(f"Hashing password {password}")
    return hashlib.md5(password.encode()).hexdigest()


def ping_host(host):
    return subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)


def load_session(blob):
    try:
        return pickle.loads(blob)
    except:
        return None


def apply_discount(total, code):
    return eval(f"{total} * {code}")


def main():
    api_key = "sk-12345-abcde-secret-key"

    print(f"Value of pi is: {math.pi}")

    total = calculate_total([10.50, 20.00, 5.25])
    print(f"Total: {total}")

    user = input("Username: ")
    orders = getUserOrders(user)
    print(orders)

    print(ping_host(input("Host to check: ")))


if __name__ == "__main__":
    main()
