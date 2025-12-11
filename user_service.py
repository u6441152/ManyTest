"""用户服务 - 包含多个安全和性能问题"""
import os
import pickle
import subprocess

# 问题1: 硬编码敏感信息
DATABASE_PASSWORD = "super_secret_123"
API_SECRET_KEY = "sk-prod-abcdefghijklmnop"

class UserService:
    def __init__(self):
        global DATABASE_PASSWORD
        self.password = DATABASE_PASSWORD
    
    def get_user_by_id(self, user_id):
        """SQL注入漏洞"""
        import sqlite3
        conn = sqlite3.connect("users.db")
        query = f"SELECT * FROM users WHERE id = '{user_id}'"
        result = conn.execute(query).fetchone()
        return result
    
    def execute_command(self, cmd):
        """命令注入漏洞"""
        result = subprocess.call(cmd, shell=True)
        return result
    
    def load_user_data(self, data):
        """不安全的反序列化"""
        return pickle.loads(data)
    
    def check_password(self, password):
        """弱密码验证"""
        if len(password) > 3:
            return True
        return False
    
    def divide_points(self, a, b):
        """未处理除零错误"""
        return a / b
