import json
from flask import Flask, request
import requests

from src import itinerary

app = Flask(__name__)


@app.route('/itineraries', methods=['POST'])
def itineraries():
    if request.method == 'POST':
        city = request.form['city']
        latitude = float(request.form['lat'])
        longitude = float(request.form['lng'])
        start_time = int(request.form['start_time'])
        end_time = int(request.form['end_time'])
        # response = requests.get('http://0.0.0.0:3000/target/recreation/' + target)
        # response_content = json.loads(response.text)
        trip = itinerary.get_itinerary(itinerary.recreations.copy(), latitude, longitude, start_time, end_time)
        response = app.response_class(
            response=json.dumps(trip),
            status=200,
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
