import datetime
import os

import jwt
import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from flask import json

from imagingSystem.settings import SECRET_KEY
from system.models import User
from django.shortcuts import render, HttpResponse


"""实现登录操作"""
@csrf_exempt
def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        if verify_credentials(username, password):
            token = get_token(username)
            login_info = {
                "message": f"user {username} login succeed",
                "token": token
            }
            return JsonResponse(login_info)
    login_info = {
        "message": "userid or password is wrong!",
    }
    return JsonResponse(login_info)


def verify_credentials(username, password):
    stored_credentials = load_credentials()
    if username in stored_credentials:
        print(username, stored_credentials[username])
        hashed_password = stored_credentials[username].encode()
        input_hashed_password = password.encode()
        if bcrypt.checkpw(input_hashed_password, hashed_password):
            print("success")
            return True
        print("failure")
    return False


def load_credentials():
    config_dir = os.path.join(os.path.expanduser('.'), 'system')
    credentials_file = os.path.join(config_dir, '.accounts')
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as f:
            credentials = json.load(f)
        return credentials
    else:
        return {}


def save_credentials(credentials):
    config_dir = os.path.join(os.path.expanduser('.'), 'config')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    credentials_file = os.path.join(config_dir, '.accounts')
    with open(credentials_file, 'w') as f:
        json.dump(credentials, f)


def get_token(username):
    login_time = datetime.datetime.now() + datetime.timedelta(hours=24)
    payload = {"username": username, "exp": login_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


"""修改密码操作"""
@csrf_exempt
def change_password(self):
    username = self.username_edit.text()
    old_password = self.old_password_edit.text()
    new_password = self.new_password_edit.text()
    confirm_password = self.confirm_password_edit.text()

    if new_password != confirm_password:
        QMessageBox.warning(self, "错误", "新密码和确认密码不一致！")
        return


def show(request):
    return HttpResponse('Hello, world. You\'re at the polls view.')