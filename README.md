# Broker Data Deletion Request Automation

This project automates the submission of the Free Data Deletion Request Form at [https://broker.sparksammy.com/](https://broker.sparksammy.com/) every 6 months using Selenium and Python.

## Features
- **Automated browser-based form submission** using headless Chrome
- **Reads your details from a `.env` file**
- **Ensures the form is only submitted once every 6 months**
- **Easy scheduling with cron**

---

## Setup

### 1. Clone the repository and navigate to the project directory

### 2. Create a `.env` file with your details:
```
FULL_NAME=Your Name
ADDRESSES=123 Main St\n456 Oak Ave
EMAILS=you@example.com,other@example.com
PHONE=123-456-7890
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

## Usage

To run the script manually:
```
python submit_broker_form.py
```

- The script will only submit the form if 6 months have passed since the last successful submission (tracked in `last_run.txt`).
- All form fields are filled using the values from your `.env` file.

---

## Scheduling with Cron

To automate the process, set up a daily cron job. The script will only submit if 6 months have passed since the last run.

Edit your crontab:
```
crontab -e
```
Add this line (adjust the Python and script path as needed):
```
0 9 * * * /usr/bin/python3 /Users/sparky/Code/broker-desktop/submit_broker_form.py
```

---

## Notes
- The script uses headless Chrome via Selenium and automatically manages the ChromeDriver.
- The `.env` file is ignored by git (see `.gitignore`).
- You can test the script manually at any time; it will not submit more than once every 6 months.

---

## Troubleshooting
- Make sure you have Google Chrome installed.
- If you encounter issues with ChromeDriver, ensure your Chrome version is up to date.
- Check that your `.env` file is correctly formatted and present in the project directory.

---

## License
SPL-R5