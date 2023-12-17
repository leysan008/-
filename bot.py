import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/release/anekdot/month/'
API_KEY = '6804806485:AAEajnpDv9VHKG3tPLqZQMiNfysFlyN6r-E'
def parser(url):
    r = requests.get(URL)
    soup = b(r.text,'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_joker = parser(URL)
random.shuffle(list_of_joker)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Приветик! Чтобы посметься введите любую цифру:')
@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, list_of_joker[0])
        del list_of_joker[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру:')
bot.polling(none_stop=True, interval=0)