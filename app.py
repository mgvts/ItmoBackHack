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
    return "123"


if __name__ == '__main__':
    app.run()
