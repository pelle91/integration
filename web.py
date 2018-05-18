from flask import Flask, request, jsonify
import api

app = Flask(__name__)


@app.route('/', methods=['POST'])
def test():
    name = 'Simin'
    restaurants = api.info(name)
    text_data = 'Restauranger nära {0}:\n\n '.format(name)
    for i in range(0, 5):
        text_data += restaurants[i] + '\n'

    data = {
        "response_type": "in_channel",
        "text": text_data
    }
    data = jsonify(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
