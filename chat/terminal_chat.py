from termcolor import colored
from pusher import Pusher
import pysher
from dotenv import load_dotenv
import os
import json
import pyperclip

load_dotenv(dotenv_path='.env')


class terminalChat():
    pusher = None
    channel = None
    chatroom = "fooska"
    clientPusher = None
    user = None


class terminalChat():
    active_users = []

    def main(self):
        self.login()
        self.initPusher()
        while True:
            self.getInput()

    def login(self):
        username = input("Please enter your username: ")
        if username in self.active_users:
            print("This username is already taken. Please choose another one.")
            self.login()
        else:
            self.active_users.append(username)
            self.user = username

    def initPusher(self):
        self.pusher = Pusher(app_id=os.getenv('PUSHER_APP_ID', None), key=os.getenv(
            'PUSHER_APP_KEY', None), secret=os.getenv('PUSHER_APP_SECRET', None), cluster=os.getenv('PUSHER_APP_CLUSTER', None))
        self.clientPusher = pysher.Pusher(
            os.getenv('PUSHER_APP_KEY', None), os.getenv('PUSHER_APP_CLUSTER', None))
        self.clientPusher.connection.bind(
            'pusher:connection_established', self.connectHandler)
        self.clientPusher.connect()

    def connectHandler(self, data):
        self.channel = self.clientPusher.subscribe(self.chatroom)
        self.channel.bind('newmessage', self.pusherCallback)

    def pusherCallback(self, message):
        message = json.loads(message)
        if message['user'] != self.user:
            print(colored("{}: {}".format(
                message['user'], message['message']), "blue"))
            print(colored("{}: ".format(self.user), "green"))

    def getInput(self):
        message = input(colored("{}: ".format(self.user), "green"))
        if message == "!exit":
            exit(0)
        elif message == "!paste":
            message = pyperclip.paste()
        self.pusher.trigger(self.chatroom, u'newmessage', {
                            "user": self.user, "message": message})


if __name__ == "__main__":
    terminalChat().main()
