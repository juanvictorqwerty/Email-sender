import pandas as pd
import smtplib
import random
from datetime import datetime

# Email credentials
EMAIL = "juanvictorqwerty@gmail.com"  # Replace with your email
PASSWORD = "mpaq clbp iosc ging "    # Replace with your App Password

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Read the birthdays data
data = pd.read_csv("birthdays.csv")

# Create a dictionary to map birthdays
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# Check if today is someone's birthday
if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]

    # Select a random letter template
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    try:
        with open(filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", person['name'])

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            connection.login(EMAIL, PASSWORD)  # Log in to the email account
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=person['email'],
                msg=f"Subject: Happy Birthday!\n\n{contents}"
            )
            print("Email sent successfully!")

    except FileNotFoundError:
        print(f"Error: The letter template file '{filepath}' was not found.")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and password.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No birthdays today.")