from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])

def weather():
    location = request.form['location']
    api_key = ''
    api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
    response = requests.get(api_url)
    weather_info = response.json()
    return render_template('weather.html', location=location, weather_info=weather_info)

def get_weather():
    city = request.form['city']
    api_key = '094285e26dd944a6b88215434231711'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    response = requests.get(url)
    weather_data = response.json()

    try:
        current_data = weather_data['current']
        temperature_celsius = current_data['temp_c']
        feelslike = current_data['feelslike_c']
        description = current_data['condition']['text']
        wind_dir = current_data['wind_dir']
        wind_speed = current_data['wind_kph']
        humidity = current_data['humidity']
        precip = current_data.get('precip_mm', 'N/A')

        return render_template('weather.html', city=city, temperature=temperature_celsius, feelslike = feelslike, description=description, wind_dir=wind_dir, wind_speed=wind_speed, humidity=humidity, precip=precip)

    except KeyError as e:
        print(f"Error: {e}")
        return render_template('weather.html', error="Error retrieving weather data. Please try again.")


if __name__ == '__main__':
    app.run(debug=True)
