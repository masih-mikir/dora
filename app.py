import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests

from src import itinerary

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/itineraries', methods=['POST'])
@cross_origin()
def itineraries():
    if request.method == 'POST':
        city = request.form['city']
        latitude = float(request.form['lat'])
        longitude = float(request.form['lng'])
        start_time = int(request.form['start_time'])
        end_time = int(request.form['end_time'])

        data = {
            'recreation_city': city
        }
        response = requests.post('http://localhost:3000/api/recreation/city', data=data)
        response_recreation = json.loads(response.text)

        data = {
            'restaurant_city':city
        }
        response = requests.post('http://localhost:3000/api/restaurant/city', data=data)
        response_restaurant = json.loads(response.text)
        print(response_recreation)
        print(response_restaurant)

        trip = itinerary.get_itinerary(response_recreation['data'], response_restaurant['data'], latitude, longitude, start_time, end_time)
        response = app.response_class(
            response=json.dumps({'data': trip}),
            status=200,
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
