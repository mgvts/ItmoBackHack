import json

import psycopg2
from pprint import pprint

factors = [""]


class BDController:
    def _start(self):
        self.file_name = "./stat.json"
        self.file = open(self.file_name, "r")

    def __init__(self):
        pass

    def getAll(self):
        self._start()
        rows = json.loads(self.file.read())
        pprint(rows)
        self._close()

        return rows

    def setData(self, data: dict):
        with open(self.file_name, "r") as f:
            base = json.loads(f.read())
        base.update(data)
        with open(self.file_name, "w") as f:
            f.write(json.dumps(base))
        return

    def _close(self):
        self.file.close()


bd = BDController()
bd.getAll()
