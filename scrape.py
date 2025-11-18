import json
import requests
from bs4 import BeautifulSoup
import os

def load_data():
    try:
        with open('scraped_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open('scraped_data.json', 'w') as f:
        json.dump(data, f, indent=4)

def handler(event, context):
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }

    try:
        body = json.loads(event['body'])
        url = body.get('url')
        selector = body.get('selector')

        if not url or not selector:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'URL and selector are required'})
            }

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.select(selector)
        scraped_data = [elem.get_text(strip=True) for elem in elements]

        if scraped_data:
            data = load_data()
            data.append({'url': url, 'selector': selector, 'data': scraped_data})
            save_data(data)
            return {
                'statusCode': 200,
                'body': json.dumps({'data': scraped_data})
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'No data found with the given selector'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Error scraping data: {str(e)}'})
        }
