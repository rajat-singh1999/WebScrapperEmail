import requests
import smtplib
import time
from bs4 import BeautifulSoup


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email id', 'password')

    subject = 'Price fell down!'
    body = f'See the amazon link: url' #copy the url
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('sender email(email that you just put in above)', 'receiver email', msg)

    print('HEY MAIL HAS BEEN SENT!')

    server.quit()


def price_tag():

    URL = 'link of your choice' #you can put the url here

    headers = {"User-Agent": 'your user agent'} #you can get your user agent by serching for it on google

    source = requests.get(URL, headers=headers)

    c_source = BeautifulSoup(source.content, 'lxml')   # you can use html parser, buts that's ok
    #
    # print(c_source.prettify())
    h = c_source.find(id='priceblock_ourprice').get_text()
    # print(h)
    s = h.strip()
    st = ''
    for i in s:
        if i == ' ' or i == ',':
            continue
        elif i == '.':
            break
        else:
            st = st + i
    st = st[1:]
    print(float(st))
    if float(st) < 17500.0:   #this is the price setting. Customize it according to your needs
        send_email()


while(True):
    price_tag()
    time.sleep(60 * 60) #this makes the program to sleep in the background for (60*60) seconds, you can change it.
