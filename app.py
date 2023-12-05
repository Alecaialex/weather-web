from flask import Flask, render_template, request
import requests
try:
    from config import API_KEY
except ImportError:
    print("You need to execute setup.py first. Press enter to exit...")
    input()
    quit()
    

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'

    response = requests.get(url)
    weather_data = response.json()

    try:
        current_data = weather_data['current']
        temperature_c = round(current_data['temp_c'])
        feelslike_c = round(current_data['feelslike_c'])
        temperature_f = round(current_data['temp_f'])
        feelslike_f = round(current_data['feelslike_f'])
        description = current_data['condition']['text']
        descriptionicon = current_data['condition']['icon']
        wind_dir = current_data['wind_dir']
        wind_speed = current_data['wind_kph']
        humidity = current_data['humidity']
        precip = current_data.get('precip_mm', 'N/A')
        isday = current_data['is_day']

        return render_template('weather.html', city=city, temperature_c=temperature_c, feelslike_c=feelslike_c,
                            temperature_f=temperature_f, feelslike_f=feelslike_f, description=description, wind_dir=wind_dir, 
                            wind_speed=wind_speed, humidity=humidity,
                            precip=precip, isday=isday, descriptionicon=descriptionicon)

    except KeyError as e:
        print(f"Error: {e}")
        return render_template('weather.html', error="Error retrieving weather data. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)