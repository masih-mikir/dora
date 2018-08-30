import json
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/itineraries', methods=['POST'])
def itineraries():
    if request.method == 'POST':
        target = request.form['target']
        longitude = request.form['lng']
        latitude = request.form['latitude']
        response = requests.get('http://0.0.0.0:3000/target/recreation/' + target)
        response_content = json.loads(response.text)
        return target


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
