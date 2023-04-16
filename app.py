from flask import Flask, request
import bdRequests as bd

app = Flask(__name__)

base = bd.BDController()


def parseData(d: [[]]) -> {"": [{}]}:
    return {i[3]: i for i in d}


@app.route('/start_time', methods=["GET"])
def get_data():
    return parseData(base.getAll()["start_time"])


@app.route('/data_size', methods=["GET"])
def get_data():
    return parseData(base.getAll()["data_size"])


@app.route('/data_per_time', methods=["GET"])
def get_data():
    return parseData(base.getAll()["data_per_time"])


@app.route('/duration', methods=["GET"])
def get_data():
    return parseData(base.getAll()["duration"])


# todo
@app.route('/addData', methods=['POST'])
def post_data():
    base.setData(request.json)
    print("here")
    print(request.json())

    return "123"


if __name__ == '__main__':
    app.run(host="164.92.210.100")
# print(parseData([[1, 1111111, 99, "Hi", "hi/hello", 123], [2, 123123, 8989, "hihi", "/hi/men/hi", None],
#                  [3, 97989, 892828, "ioio", "/ioi/www/www/oo", 9]]))
    app.run()
