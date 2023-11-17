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

if __name__ == '__main__':
    app.run(debug=True)
