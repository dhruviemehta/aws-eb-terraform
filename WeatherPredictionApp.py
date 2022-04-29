import requests
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
cities=["Mumbai","Dubai"]

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    r = requests.get(url).json()
    return r

@app.route('/')
def index_get():
    weather_data = []

    for city in cities:

        r = get_weather_data(city)
        ##print(r)

        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data)

@app.route('/', methods=['POST'])
def index_post():
    err_msg = ''
    new_city = request.form.get('city')
        
    if new_city not in cities:
        new_city_data = get_weather_data(new_city)

        if new_city_data['cod'] == 200:
            cities.append(new_city)
        else:
            err_msg = 'City does not exist in the world!'
    else:
        err_msg = 'City already exists in the database!'

    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added succesfully!')

    return redirect(url_for('index_get'))

@app.route('/delete/<name>')
def delete_city(name):
    cities.remove(name)

    flash(f'Successfully deleted { name }', 'success')
    return redirect(url_for('index_get'))

if __name__ == '__main__':
   app.run(debug = True)