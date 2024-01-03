# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from base_classes.data_functions import Functions

load_dotenv()


class Bot:
    def __init__(self, bot_name: str):
        self.functions = Functions()

    def run(self):
        username = input("Username:")
        email = input("Email:")
        password = input("Password:")
        self.functions.registration(username=username, email=email, password=password)
        self.functions.auth(username=username, password=password)
        title = input("Title:")
        content = input("Content:")
        self.functions.add_post(title=title, content=content)


if __name__ == '__main__':
    Bot("onlinecontract").run()
