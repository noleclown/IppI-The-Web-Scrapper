# TODO: Build and Host Web Scraper Agent on Netlify

## Steps to Complete
- [x] Create app.py: Main Flask application with scraping logic, routes for input and display, data saving to JSON.
- [x] Create templates/index.html: HTML template for the web interface (form for URL and selectors, display results).
- [x] Create static/styles.css: Basic CSS for styling the interface.
- [x] Create requirements.txt: List of Python dependencies (Flask, requests, beautifulsoup4).
- [x] Create Procfile: For Heroku deployment to specify the web process.
- [x] Create runtime.txt: Specify Python version for Heroku.
- [x] Install dependencies locally using pip install -r requirements.txt.
- [x] Test the app locally by running flask run and using browser_action to verify functionality. (App is running on http://127.0.0.1:5000)
- [x] Thorough testing: UI renders correctly, scraping works (tested with example.com), data saves to JSON, error handling for invalid inputs.
- [x] Adapt for Netlify: Convert to static site with Netlify Functions for scraping.
- [x] Create public/index.html: Static HTML for the interface.
- [x] Create netlify/functions/scrape.py: Serverless function for scraping logic.
- [x] Create netlify.toml: Configuration for Netlify deployment.
- [x] Update requirements.txt for Netlify Functions.
- [x] Create public/styles.css: Copy CSS to public folder.
- [x] Thorough testing: Static HTML interface (form renders), Netlify Function (scrapes example.com successfully), data saving (persists to JSON locally).
- [ ] Deploy to Netlify: Push to GitHub, connect to Netlify, deploy.
