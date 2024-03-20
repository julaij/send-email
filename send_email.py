import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append(dict(zip(headers, row)))
    return data

def send_email(sender_email, sender_password, receiver_email, subject, message):
    smtp_server = 'smtp.gmail.com'  # Change this if using a different SMTP server
    smtp_port = 587  # Change this if using a different port

    # Setup SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Construct email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    # Read data from CSV
    data = read_csv('data.csv')

    # Email configuration
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
    receiver_email = 'recipient@example.com'
    subject = 'Data from CSV file'
    
    # Construct email message
    message = "Hello,\n\n"
    for row in data:
        message += f"Name: {row['Name']}, Email: {row['Email']}, Age: {row['Age']}\n"

    # Send email
    send_email(sender_email, sender_password, receiver_email, subject, message)
    print("Email sent successfully!")
