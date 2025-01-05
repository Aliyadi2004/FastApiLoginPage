from Model import *


class main:
    def __init__(self):
        self.model = Model()

    def sinup(self, name, password):
        self.model.store(f"INSERT INTO login(username, password) VALUES ('{name}', '{password}')")
        print("finsh")

    def login(self, name, password):
       
        chekingMembers= self.model.restore(f"SELECT * FROM login WHERE login.username = '{name}' AND login.password = '{password}'")
        return chekingMembers