from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def fetch_data():
    # Making connection to the database
    conn = psycopg2.connect(
        host='scraper_database',
        user='postgres',
        password='scraperdatabase',
        database='scraper',
        port='5432'
    )
    cursor = conn.cursor()

    # A list of tuples representing the fetched data each containing title and image_url
    cursor.execute("SELECT title, image_url FROM scraped LIMIT 500")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

@app.route('/')
def index():
    # Renders the index.html template with the data fetched from the database
    data = fetch_data()
    return render_template('/index.html', data=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
