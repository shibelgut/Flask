from flask import Flask, render_template  # подключаем модуль и render_template, который включает функции для Jinja
from data import tours, departures

app = Flask(__name__)  # объявляем экземпляр flask


@app.route('/')  # объявляем путь /
def main():
    return render_template('index.html')


@app.route('/departures/')
def direction():
    return render_template('departure.html')


@app.route('/tours/')
def tour():
    return render_template('tour.html')


@app.route('/data/')
def data():
    # for key in tours:
    #     t = tours[key]
    #     id_list = []
    #     title_list = []
    #     price_list = []
    #     stars_list = []
    #     country_list = []
    #     for k in t:
    #         id_list.append(key)
    #         if k == 'title':
    #             title_list.append(t[k])
    #         if k == 'price':
    #             price_list = t[k]
    #         if k == 'stars':
    #             stars_list = t[k]
    #         if k == 'country':
    #             country_list = t[k]
    #     output = render_template('data.html', country= country_list, id=id_list, title=title_list, price=price_list, stars=stars_list)
    #     return output
    tours_list = []
    for t in tours:
        tours_list.append(tours[t])
    output = render_template('data.html', tours=tours_list)
    return output


@app.route('/data/departures/<name_departure>/')
def departure(name_departure):
    tours_list = []
    for t in tours:
        tours_list.append(tours[t])
    tours_departure_list = []
    for s in tours_list:
        if s["departure"] == name_departure:
            tours_departure_list.append(s)
            destination = departures[name_departure]
    output = render_template('name_departure.html', destination=destination, departure=name_departure, tours=tours_departure_list)
    return output


@app.route('/data/tours/<int:id_tour>/')
def tours_id(id_tour):
    t = tours[id_tour]
    for k in t:
        if k == 'title':
            title = t[k]
        if k == 'price':
            price = t[k]
        if k == 'nights':
            nights = t[k]
        if k == 'country':
            country = t[k]
        if k == 'description':
            description = t[k]
    output = render_template('id.html', country=country, title=title, price=price, nights=nights, description=description)
    return output


app.run()
