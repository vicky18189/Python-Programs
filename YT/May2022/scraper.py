import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.wakefit.co/mattress/orthopaedic-memory-foam-mattress/WOMFM75728'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="product_name").get_text()
    dimensions = soup.find(id="product_dimensions").get_text()
    price = soup.find(itemprop="price").get_text()
    converted_price = float(price[0:7])
    product= title + dimensions 

    print(title + dimensions)
    print(converted_price)

    if(converted_price < 13160):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vicky18189@gmail.com','qaqbjghwkniyfwre')

    subject = 'Price fell down!'
    body = f"Check the price of the mattress is now down open link: https://www.wakefit.co/mattress/orthopaedic-memory-foam-mattress/WOMFM75728"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('vicky18189@gmail.com', 'vicky18189@gmail.com',msg)

    print('Email has been sent!')
    server.quit()

while (True):
    check_price()
    time.sleep(5)