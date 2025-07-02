import requests
from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load US CPI data (Consumer Price Index by year)
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data/cpi_us.csv')
cpi_df = pd.read_csv(DATA_PATH)
cpi_df.set_index('Year', inplace=True)

# Get current exchange rates (base: USD)
EXCHANGE_API_KEY = '027e8bd24ef287404960d077'
EXCHANGE_API_URL = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD'

def get_exchange_rates():
    response = requests.get(EXCHANGE_API_URL)
    if response.status_code == 200:
        return response.json().get('conversion_rates', {})
    return {}

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        amount = amount / rates.get(from_currency, 1)
    return amount * rates.get(to_currency, 1)

def adjust_inflation_usd(amount, from_year, to_year):
    if from_year not in cpi_df.index or to_year not in cpi_df.index:
        return None
    from_cpi = cpi_df.loc[from_year, 'CPI']
    to_cpi = cpi_df.loc[to_year, 'CPI']
    return amount * (to_cpi / from_cpi)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    from_year = int(request.form['from_year'])
    to_year = int(request.form['to_year'])

    rates = get_exchange_rates()
    usd_today = convert_currency(amount, from_currency, 'USD', rates)
    usd_target_year = adjust_inflation_usd(usd_today, 2025, to_year)
    target_amount = convert_currency(usd_target_year, 'USD', to_currency, rates)

    return render_template('result.html', result=round(target_amount, 2),
                           from_currency=from_currency, to_currency=to_currency,
                           from_year=from_year, to_year=to_year, original_amount=amount)

if __name__ == '__main__':
    app.run(debug=True)