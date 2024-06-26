from flask import Flask, render_template, flash, redirect, url_for, get_flashed_messages

posts_list = [
    {
        'title': 'Paragraf 1',
        'content': 'Rój pszczół staje się niczyim, jeżeli właściciel nie odszukał go przed upływem trzech dni od dnia wyrojenia. Właścicielowi wolno w pościgu za rojem wejść na cudzy grunt, powinien jednak naprawić wynikłą stąd szkodę.'
    },
    {
        'title': 'Paragraf 2',
        'content': 'Jeżeli rój osiadł w cudzym ulu nie zajętym, właściciel może domagać się wydania roju za zwrotem kosztów'
    },
    {
        'title': 'Paragraf 3',
        'content': 'Jeżeli rój osiadł w cudzym ulu zajętym, staje się on własnością tego, czyją własnością był rój, który się w ulu znajdował. Dotychczasowemu właścicielowi nie przysługuje w tym wypadku roszczenie z tytułu bezpodstawnego wzbogacenia. '
    }
]

products_list = [
    {"name": "Janosik 7.3%", "price": 3.70, "stock": 5},
    {"name": "Blachotrapez", "price": 100, "stock": 0},
    {"name": "Mega rollo mieszany mieszany", "price": 20, "stock": 3},
    {"name": "Kurczak curry z mekonga", "price": 35, "stock": 0},
    #{"name": "Nissan Micra", "price": 3000, "stock": 1}
]

app = Flask(__name__)
app.secret_key="klucz"
@app.route('/')
def index():
    return render_template('index.html', name="Strona główna", posts=posts_list)

@app.route('/contact')
def contact():
    return render_template('contact.html',name="Kontakt", adress="Kalinowa 7", phone="530708858")

@app.route('/shop')
def shop():
    return render_template('shop.html',name="Sklep", products=products_list)

@app.route('/like_facebook', methods=['POST'])
def like_facebook():
    flash('Dzięki za polubienie!')
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)