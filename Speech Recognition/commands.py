import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                print("You haven't told me your name yet!")
            print("My name is Python Commander. How are you?")
        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            self.respond("Opening " + app)
            os.system("start " + app + ".exe")

    def respond(self, response):
        print(response)
