from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from wikipediaconnector import search_wikipedia

app = Flask(__name__, static_folder='static')
app.debug = True

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'JosephStalin1878!',
    'database': 'regostration'
}

# No need to create the MySQL connection object and cursor here

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        query = "SELECT user_email, user_password FROM regostration;"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            if email == row[0] and password == row[1]:
                return redirect('/mainpage')
        
        return redirect(url_for('images'))

    return render_template('signup.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')

        if password != repeat_password:
            return render_template('registration.html')  # You can provide appropriate error handling

        query = "INSERT INTO regostration(user_email, user_password, confirm_password) VALUES (%s, %s, %s)"
        values = (email, password, repeat_password)
        cursor.execute(query, values)
        conn.commit()
        return redirect(url_for('mainpage'))  # You can provide a success message

    return render_template('registration.html')


@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():  
    if request.method == "POST":
        quiry = request.form.get('quiry')
        serch_results = search_wikipedia(quiry)
        return render_template('mainpage.html', result=serch_results)
    
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run()   
