import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta

# Load environment variables from .env
load_dotenv()
FULL_NAME = os.getenv('FULL_NAME')
ADDRESSES = os.getenv('ADDRESSES')
EMAILS = os.getenv('EMAILS')
PHONE = os.getenv('PHONE')

# File to store last run date
LAST_RUN_FILE = 'last_run.txt'

def ran_within_6_months():
    if not os.path.exists(LAST_RUN_FILE):
        return False
    with open(LAST_RUN_FILE, 'r') as f:
        last_run = f.read().strip()
    last_run_date = datetime.strptime(last_run, '%Y-%m-%d')
    return datetime.now() < last_run_date + relativedelta(months=6)

def update_last_run():
    with open(LAST_RUN_FILE, 'w') as f:
        f.write(datetime.now().strftime('%Y-%m-%d'))

def main():
    if ran_within_6_months():
        print('Script ran within the last 6 months. Exiting.')
        return

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://broker.sparksammy.com/')
    time.sleep(6)  # Wait for page to load

    # Fill Full Name
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys(FULL_NAME)

    # Fill Addresses
    addresses_input = driver.find_element(By.ID, "addresses")
    addresses_input.send_keys(ADDRESSES.replace('\\n', '\n'))

    # Fill Email Addresses
    emails_input = driver.find_element(By.ID, "emails")
    emails_input.send_keys(EMAILS)

    # Fill Phone Number
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys(PHONE)

    # Submit the form
    submit_btn = driver.find_element(By.ID, "submitButton")
    submit_btn.click()

    time.sleep(2)  # Wait for submission
    driver.quit()
    update_last_run()
    print('Form submitted successfully.')

if __name__ == '__main__':
    main() 