# Zoho Invoice Automation with Selenium

This Python script automates the process of logging into Zoho Invoice, entering invoice details, and saving the invoice using the Selenium web automation framework.

## Prerequisites

Before using this script, you should have the following prerequisites in place:

1. **Zoho Invoice Account**: To use this script, you need to have a Zoho Invoice account. If you don't have one, you can sign up for a Zoho Invoice account at [Zoho Invoice](https://www.zoho.com/invoice/).

2. **Chrome Web Driver**: Download the Chrome Web Driver and place it in your desired location. Make sure to update the `executable_path` in the script to point to your Chrome Web Driver. You can download it from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).

3. **Configuration File**: Create a configuration file named `config.yaml` with the following format:

```yaml
username: your_zoho_invoice_username
password: your_zoho_invoice_password
```

## Usage

1. Create a Zoho Invoice account if you don't have one.

2. Create a configuration file named `config.yaml` with your Zoho Invoice username and password.

3. Execute the script by running it with Python.

```bash
python script_name.py
```

## Script Overview

- `load_configuration`: Reads the username and password from the `config.yaml` file.
- `login_zoho_invoice`: Logs into Zoho Invoice using the provided credentials.
- `enter_authorization_code`: Enters the authorization code when prompted.
- `click_trust_button`: Clicks the 'Trust' button.
- `skip_weekends`: Function to skip weekends and calculate the end date accordingly.
- `week_number_and_dates`: Calculates the week number and dates for the current week.
- `add_invoice_details`: Fills in the invoice details, including week information, rate per hour, and the number of hours worked per week.
- `save_invoice`: Saves the invoice.
- `wait_for_invoice_creation`: Waits for the invoice to be created successfully.

## Customization

You can customize the script to suit your specific needs. For example, you can modify the invoice details, browser settings, or error handling as required.

Please note that web scraping and automation may be subject to website terms of service. Use this script responsibly and in compliance with Zoho's terms and conditions.

## Using the Script for Invoicing

This script is designed to create invoices for services based on an hourly rate and the number of hours worked per week. To use it effectively:

1. Ensure that your Zoho Invoice account is set up with the appropriate details, including your hourly rate.

2. Configure your `config.yaml` file with your Zoho Invoice username and password.

3. Run the script, and it will log in, create a new invoice, and populate it with the week's details, including the week number, dates, hourly rate, and the number of hours worked per week.

4. Review the generated invoice to ensure accuracy and click 'Save' in Zoho Invoice to finalize the invoice creation.
# zohobooks-auto-invoice-bot
# zohobooks-auto-invoice-bot
# zohobooks-auto-invoice-bot
