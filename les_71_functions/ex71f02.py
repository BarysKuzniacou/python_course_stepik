def send_mail(message, messanger):
    topic = 'e-mail: '
    print(topic + message + ' from ' + messanger)


text = 'Hi'
send_mail(text, 'Ivan')