from flask import Flask, render_template, request
import requests

app = Flask(__name__)


f72322cb9amsh83bfbc817491cc9p19ec12jsnb9d7fcd82d45 = 'f72322cb9amsh83bfbc817491cc9p19ec12jsnb9d7fcd82d45'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_destinations', methods=['POST'])
def get_destinations():
    preferences = request.form.to_dict()
    destination_type = preferences['destination_type']

    
    tripadvisor_url = f''https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport',
  params: {query: 'london'},
  headers: {
        'X-RapidAPI-Host': 'tripadvisor16.p.rapidapi.com',
        'X-RapidAPI-Key': f72322cb9amsh83bfbc817491cc9p19ec12jsnb9d7fcd82d45
    }
    response = requests.get(tripadvisor_url, headers=headers)
    destinations_data = response.json()

   
    recommended_destinations = []
    for destination in destinations_data['data']:
        destination_name = destination['result_object']['name']
        destination_location = destination['result_object']['location_string']

        
        openweather_url = f'https://open-weather13.p.rapidapi.com/city/landon'&appid=f72322cb9amsh83bfbc817491cc9p19ec12jsnb9d7fcd82d45'
        weather_response = requests.get(https://open-weather13.p.rapidapi.com/city/landon')
        weather_data = weather_response.json()
        weather_description = weather_data['weather'][0]['description']
        
        recommended_destinations.append({
            'name': destination_name,
            'location': destination_location,
            'weather': weather_description
        })

    return render_template('result.html', recommended_destinations=recommended_destinations)

if __name__ == '__main__':
    app.run(debug=True)
