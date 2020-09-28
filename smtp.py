import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ^ и $ Концы строк
# \w+ проверка что почта начинается с символа
# ([\.-]?\w+) Условие на наличие только 1-ой точки подряд
# (\.\w{2,3}) Поиск точки и проверка на наличие 2-3 любых символов + завершение осмотра
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
login = '***'
password = '***'
url = 'smtp.mail.ru'
server = smtplib.SMTP_SSL(url, 465)  # подключение к SSL + порт
server.login(login, password)  # авторизация в почтовом ящике

def send_mail():
    toaddr=input ('Кому: ') # Почта получтеля
    if (re.search(regex, toaddr)):
        print("Valid Email")
        topic = input("Тема: ")  # Тема письма
        message = input("Введите сообщение: ")  # Сообщение


        msg = MIMEMultipart()
        msg['Subject'] = topic
        msg['From'] = login
        body = message
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(login, toaddr, msg.as_string())  # Отправка (от кого, кому, что)
    else:
        print("Invalid Email")

send_mail() #Вызов процедуры
