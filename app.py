from flask import Flask, jsonify
import scrapp, json



app = Flask(__name__)


@app.route('/<string:name>', methods=['GET'])
def main(name):

    data = scrapp.scrapp(name)
    print(type(data))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
