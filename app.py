from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import json
import os

app = Flask(__name__)

DATA_FILE = 'scraped_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        selector = request.form.get('selector')
        if not url or not selector:
            return render_template('index.html', error="URL and selector are required.")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.select(selector)
            scraped_data = [elem.get_text(strip=True) for elem in elements]
            if scraped_data:
                data = load_data()
                data.append({'url': url, 'selector': selector, 'data': scraped_data})
                save_data(data)
                return render_template('index.html', success="Data scraped and saved successfully.", data=scraped_data)
            else:
                return render_template('index.html', error="No data found with the given selector.")
        except Exception as e:
            return render_template('index.html', error=f"Error scraping data: {str(e)}")
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
