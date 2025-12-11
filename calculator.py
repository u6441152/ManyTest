# 简单计算器 - 包含一些待审查的问题

import os
import sys
import json  # 未使用的导入

def add(a, b):
    return a + b

def divide(x, y):
    # 没有处理除零错误
    return x / y

def get_user_data(user_id):
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL 注入风险！
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    # 忘记关闭数据库连接
    return result

def process_items(items):
    total = 0
    # 低效的循环方式
    for i in range(len(items)):
        total = total + items[i]
    return total

def read_config():
    # 硬编码的密码（安全问题）
    password = "admin123"
    api_key = "sk-1234567890abcdef"
    return {"password": password, "api_key": api_key}

class Calculator:
    def __init__(self):
        self.result = 0
    
    def calculate(self, a, b, op):
        # 使用 eval 存在安全风险
        return eval(f"{a} {op} {b}")

if __name__ == "__main__":
    print(add(1, 2))
    print(divide(10, 0))  # 这会报错
