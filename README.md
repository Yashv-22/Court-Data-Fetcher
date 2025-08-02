# 🏛️ Court Case Data Fetcher & Mini Dashboard

A Flask-based web app to fetch and display court case metadata from Indian courts using case type, number, and filing year. It features a modern UI, stores queries, and supports PDF downloads.

---

## 🚀 Features

- 🔎 Fetch parties, filing date, next hearing date
- 🧾 Download latest order/judgment PDF
- 💾 Log user queries in SQLite
- 💡 Modern, responsive interface
- ❌ Handles invalid entries or site issues

---

## 📸 Demo Screenshot

![Screenshot](static/demo.png) <!-- optional: add if available -->

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3
- **Backend:** Python Flask
- **Database:** SQLite
- **Libraries:** Requests, BeautifulSoup4

---

## 🧰 Requirements

- Python 3.8+
- pip (Python package manager)

---

## 🔧 Setup Guide (Step-by-Step)

### 1. 📥 Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/court-data-fetcher.git
cd court-data-fetcher

**2. 🐍 Create & Activate Virtual Environment**
python -m venv venv
venv\Scripts\activate         # On Windows
# OR
source venv/bin/activate     # On Mac/Linux

**3. 📦 Install Dependencies**
pip install -r requirements.txt

**4. 🛠️ Initialize the Database**
python init_db.py

**5. 🚀 Run the Flask App**
python app.py
Visit http://127.0.0.1:5000 in your browser.

**📁 File Structure**
court_data_fetcher/
├── app.py
├── schema.sql
├── init_db.py
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   ├── result.html
│   └── stored_responses.html
└── requirements.txt
