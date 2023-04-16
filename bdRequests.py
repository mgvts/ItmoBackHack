import psycopg2


class BDController:
    def _start(self):
        self.conn = psycopg2.connect(database="***", user="***", password="***", host="***",
                                     port="***")
        self.cur = self.conn.cursor()
        self.AllData = 'public."AllData"'

    def __init__(self):
        pass

    def getAll(self):
        self._start()
        self.cur.execute(f'SELECT * FROM {self.AllData}')
        rows = self.cur.fetchall()
        self.close()
        return rows

    def setData(self, data: dict):
        self._start()
        self.cur.execute(
            f"INSERT INTO {self.AllData} (id, start_time, duration, name, url, data_size)"
            f" VALUES (data[id], data[start_time], data[duration], data[name], data[url], data[data_size])")
        self.conn.commit()
        self.close()
        return

    def close(self):
        self.conn.close()
