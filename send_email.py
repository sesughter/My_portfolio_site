import smtplib, ssl

host = "smtp.gmail.com"
port = "465"

username = "siortsor@gmail.com"
password = "vhvy rsme ewcn xddf"

context = ssl.create_default_context()
receiver = "sesughiortsor@gmail.com"
message = '''
hi
how are you
thank you, good bye
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)