from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lan=es&appid=7b3a3aacea0a6f77258ad667236054a9'
    
    r = requests.get(url)
    data = r.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    return render_template('index.html', city=city, temperature=temp, description=description, wind=wind, humidity=humidity, pressure=pressure)

if __name__ == '__main__':
    app.run(debug=True)