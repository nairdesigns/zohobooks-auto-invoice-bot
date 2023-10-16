from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import random
import yaml

def load_configuration(file_path):
    with open(file_path, 'r') as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)

def login_zoho_invoice(driver, username, password):
    print("Navigating to the Zoho Invoice login page...")
    driver.get("https://books.zoho.com/app/782051836#/invoices/new")
    
    print("Entering the username...")
    username_field = driver.find_element(By.ID, "login_id")
    username_field.send_keys(username)

    print("Clicking the 'Next' button to proceed to the password entry...")
    next_button = driver.find_element(By.CSS_SELECTOR, "button.btn.blue#nextbtn")
    next_button.click()
    
    print("Waiting for the password input field to appear...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    
    # Wait for the login form to load
    print("Entering the password...")
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys(password)

    print("Clicking the 'Sign in' button...")
    # Wait for the "Sign in" button to become interactable
    signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nextbtn")))
    signin_button.click()
    
    print("Waiting for the login to complete...")
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "signin_submit")))
    print("Login successful.")

def enter_authorization_code(driver):
    authorization_code = input("Enter your authorization code: ")
    print("Authorization code entered:", authorization_code)
    
    input_field = driver.find_element(By.CLASS_NAME, "splitedText")
    input_field.send_keys(authorization_code)
    
    while True:
        try:
            # Select the "Verify" button
            verify_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.blue#nextbtn')
            verify_button.click()
            print("Clicked the 'Verify' button successfully.")
            break  # Exit the loop if successful
        except Exception as e:
            print("Button not found or an error occurred:", str(e))
            print("Retrying...")

def click_trust_button(driver):
    while True:
        try:
            trust_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Trust']")))
            trust_button.click()
            print("Clicked the 'Trust' button successfully.")
            break  # Exit the loop if successful
        except Exception as e:
            print("Trust button not found or an error occurred:", str(e))
            print("Retrying...")

def current_week_number():
    today = datetime.date.today()
    
    # Calculate the start date (Monday) of the current week
    if today.day <= 15:
        # First half of the month, start from the beginning of the month
        start_date = today.replace(day=1)
    else:
        # Second half of the month, start from the first Monday after the 15th
        next_month = today.replace(day=15) + datetime.timedelta(days=1)
        while next_month.weekday() != 0:  # 0 represents Monday
            next_month += datetime.timedelta(days=1)
        start_date = next_month
    
    # Calculate the week number
    current_week_number = (today - start_date).days // 7 + 1

    return current_week_number

def get_week_number():
    if first_half_of_month():
        week_number = 1
    else:
        # Find the week number of the first Monday after the 15th
        day = 16  # Start from 16th day
        while date(today.year, today.month, day).weekday() != 0:  # 0 is Monday
            day += 1
        week_number = date(today.year, today.month, day).isocalendar()[1]
    
    return week_number

def first_half_of_month():
    today = datetime.date.today()
    # Calculate the midpoint day of the month (15th)
    midpoint_day = datetime.date(today.year, today.month, 15)
    
    # Compare today's date with the midpoint
    if today <= midpoint_day:
        return True
    else:
        return False

# Function to skip weekends and calculate the end date accordingly
def skip_weekends(start_date, days_to_skip):
    end_date = start_date
    while days_to_skip > 0:
        end_date += datetime.timedelta(days=1)
        if end_date.weekday() < 6:  # Check if it's not a weekend (0=Sunday, 6=Saturday)
            days_to_skip -= 1
    return end_date

def last_week_of_current_month():
    now = datetime.now()
    year = now.year
    month = now.month
    _, last_day = calendar.monthrange(year, month)
    last_week = (last_day - 1) // 7 + 1
    return last_week

def insert_week_number_and_date_range(week_number=None):
    today = datetime.date.today()
    
    # Calculate the start date (Monday) and end date (Friday) of the current week
    if today.day <= 15:
        # First half of the month, start from the beginning of the month
        start_date = today.replace(day=1)
    else:
        # Second half of the month, start from the first Monday after the 15th
        next_month = today.replace(day=15) + datetime.timedelta(days=1)
        while next_month.weekday() != 0:  # 0 represents Monday
            next_month += datetime.timedelta(days=1)
        start_date = next_month
        
    end_date = start_date + datetime.timedelta(days=4)

    # Skip weekends
    end_date = skip_weekends(start_date, (end_date - start_date).days)

    # Format the output
    month_name = today.strftime("%B")
    week_range = f"{start_date.day} - {end_date.day}"
    return f"Week {week_number}: {month_name} {week_range}"

def add_invoice_details(driver,week_number):
    hours_worked_this_week = round(random.uniform(29.5, 30), 2)
    driver.implicitly_wait(10)
    print("Implicitly waiting for 10 seconds")
    
    element = driver.find_element(By.CLASS_NAME, "zb-invoice-item-textarea")
    element.send_keys(insert_week_number_and_date_range(weak_number))
    print("Entered '" + insert_week_number_and_date_range() + "' in the invoice item textarea")
    
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            qty_element = driver.find_element(By.CLASS_NAME, "qty-field")
            qty_element.clear()
            qty_element.send_keys(hours_worked_this_week)
            print("Entered '" + hours_worked_this_week +"' in the quantity field")
            break
        except StaleElementReferenceException:
            attempts += 1
            print("StaleElementReferenceException occurred. Retrying...")
    
    attempts = 0
    while attempts < max_attempts:
        try:
            rate_element = driver.find_element(By.CSS_SELECTOR, '[data-integrity="line_items.0.rate"]')
            rate_element.clear()
            rate_element.send_keys("30")
            print("Entered '30' in the rate field")
            break
        except StaleElementReferenceException:
            attempts += 1
            print("StaleElementReferenceException occurred. Retrying...")
    
    element = driver.find_element(By.CLASS_NAME, "btn.btn-md")
    element.click()
    print("Clicked the 'btn.btn-md' button")
    
    invoice_row_complete = True
def save_invoice(driver):
    save_button = driver.find_element(By.ID, "save_invoice")
    save_button.click()

def is_last_week_of_month():
    today = datetime.date.today()
    next_month = today.replace(day=28) + datetime.timedelta(days=4)  # Go to the last day of the current month
    return today.month != next_month.month

def wait_for_invoice_creation(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "invoice_created_message")))
    print("Invoice created successfully")

if __name__ == "__main__":
    config = load_configuration('config.yaml')
    username = config['username']
    password = config['password']
    path_to_driver = config['path_to_driver'] 
    driver = webdriver.Chrome(executable_path=path_to_driver)
    print("Starting Selenium script")
    pass
    # Run the code:
    try:
        login_zoho_invoice(driver, username, password)
        enter_authorization_code(driver)
        click_trust_button(driver)
        current_week_number = current_week_number()
        while True:
            week_number = get_week_number()
            add_invoice_details(driver, week_number)
            week_number += 1

            if week_number == last_week_of_current_month() + 1:
                break
        save_invoice(driver)
        wait_for_invoice_creation(driver)
    except (NoSuchElementException, TimeoutException) as e:
        print("Error in login process. Retrying...")
