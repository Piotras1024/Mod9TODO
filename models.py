import json


class Domowe_wydatki:
    def __init__(self):
        try:
            with open("Domowe_wydatki.json", "r") as f:
                self.domowe_wydatki = json.load(f)
        except FileNotFoundError:
            self.domowe_wydatki = []

    def all(self):
        return self.domowe_wydatki

    def get(self, id):
        return self.domowe_wydatki[id]

    def create(self, data):
        data.pop('csrf_token')
        self.domowe_wydatki.append(data)

    def save_all(self):
        with open("Domowe_wydatki.json", "w") as f:
            json.dump(self.domowe_wydatki, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.domowe_wydatki[id] = data
        self.save_all()


domowe_wydatki = Domowe_wydatki()