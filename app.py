from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch_case_details():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    # Mock scraping (replace with actual selectors/CAPTCHA bypass)
    url = f"https://example.com/{case_type}/{case_number}/{filing_year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Simulated data (update with real scraping)
    parties = "Party A vs Party B"
    filing_date = "01-Jan-2024"
    next_hearing_date = "15-Aug-2025"
    pdf_link = "https://example.com/order.pdf"

    # Store in DB
    conn = sqlite3.connect('court_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO queries (case_type, case_number, filing_year, response) VALUES (?, ?, ?, ?)",
              (case_type, case_number, filing_year, response.text))
    conn.commit()
    conn.close()

    return render_template('result.html',
                           parties=parties,
                           filing_date=filing_date,
                           next_hearing_date=next_hearing_date,
                           pdf_link=pdf_link)

@app.route('/stored_responses')
def stored_responses():
    conn = sqlite3.connect('court_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM queries")
    queries = c.fetchall()
    conn.close()
    return render_template('stored_responses.html', queries=queries)

if __name__ == '__main__':
    app.run(debug=True)
