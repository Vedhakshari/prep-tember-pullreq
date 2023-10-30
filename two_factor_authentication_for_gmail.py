import smtplib
import random

# Generate a random 6-digit verification code
verification_code = str(random.randint(100000, 999999))

# Sender and recipient email addresses
sender_email = "your_email@gmail.com"
recipient_email = "recipient_email@gmail.com"  # The user's email

# Gmail SMTP server and port
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Gmail account username and password (use an "App Password" for added security)
smtp_username = "your_email@gmail.com"
smtp_password = "your_password"

# Create an SMTP session
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Compose the email message with the verification code
message = f"Subject: 2FA Verification Code\n\nYour verification code is: {verification_code}"

# Send the email
server.sendmail(sender_email, recipient_email, message)

# Close the SMTP session
server.quit()

# Verify the code with the user's input
user_input = input("Enter the 6-digit verification code sent to your email: ")
if user_input == verification_code:
    print("Verification successful. You can now proceed.")
else:
    print("Verification failed. Please try again.")
