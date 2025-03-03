from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    country = request.form.get('country')
    city = request.form.get('city')

    api_key = 'e98333a54e1542afaa2230535250303'  # Vervang dit met je eigen WeatherAPI-sleutel

    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city},{country}&days=3'

    response = requests.get(url)
    data = response.json()

    forecast_days = data['forecast']['forecastday']

    return render_template('forecast.html', country=country, city=city, forecast_days=forecast_days)

if __name__ == '__main__':
    app.run(debug=True)