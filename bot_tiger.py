import time
import random
import json,requests
import telebot
from datetime import datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import bd


api_key = '7745850807:AAGQzwzIDeLSbXSXnP2rOsOxIbS4920Ihg0' # Neste campo tenho que colocar a API do BotFather!
chat_id = '-107745850807' # Neste campo tenho que colocar o ID do meu canal!

bot = telebot.TeleBot(token=api_key)

def ALERT_GALE1():
    h = datetime.now().hour
    m = datetime.now().minute+1
    s = datetime.now().second
    if h <= 9:
        h =  f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    message_id = bot.send_message(chat_id=chat_id, text=f'''NOVA ENTRADA EM {h}:{m}:{s} GERANDO ENTRADA...''' ).message_id
    bd.message_ids1 = message_id
    bd.message_delete1 = True
    return

def DELETE_GALE1():
    if bd.message_delete1 == True:
        bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
        bd.message_delete1 = False

while True:
    h = datetime.now().hour
    m = datetime.now().minute+4
    s = datetime.now().second
    if h <= 9:
        h =  f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')
    cores = ['⭐️','🟦','🟦','🟦','🟦','🟦','🟦','🟦','🟦','🟦','⭐️','🟦','🟦','🟦','🟦','🟦','🟦','🟦','🟦','🟦','⭐️','🟦','🟦','🟦','🟦']

    for i in range (25):
        sample = random.sample(cores, k=25)
        print(sample[0], sample[1], sample[2], sample[3], sample[4], sample[5], sample[6], sample[7], sample[8],sample[9], sample[10], sample[11], sample[12], sample[13], sample[14], sample[15], sample[16], sample[17], sample[18], sample[19], sample[20], sample[21], sample[22], sample[23], sample[24])

        def button_link():

            markup = InlineKeyboardMarkup()

            markup.row_width = 2

            markup.add(InlineKeyboardButton(text=f"📲 Cadastre-se Pagando Muito", url="https://playpix.com/affiliates/?btag=1232096"))
            return markup

    dados = bot.send_message(chat_id=chat_id, text=(f'''
ENTRADA CONFIRMADA
    
🐯 Fortune Tiger
💻 SITE: PlayPix
⏱ 𝙑𝙖́𝙡𝙞𝙙𝙤 𝙖𝙩𝙚́: {h}:{m} 

👉 7x Normal
⚡ 6x Turbo
🚥 Intercalando

'''),
                reply_markup=button_link()) #acima é a mensagem que será exibida no telegram!
    time.sleep(240)# Aqui é a duração do sinal no caso é 4 minutos, 240 segundos!
    dados = bot.send_message(chat_id=chat_id, text=(f'''
    💸𝙎𝙞𝙣𝙖𝙡 𝙛𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙙𝙤💸
    🐯Fortune Tiger
    ⏱𝙁𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙙𝙤 𝙖́𝙨: {h}:{m}

Cadastre-se
e faça um deposito minimo
de R$ 50,00 e tenha direito a nossa
sala VIP 24 hora.
Só Chamar @suportevendas24h
    '''),
                reply_markup=button_link())# Aqui o bot deleta a mensagem anterior para ficar mais clean!
    
    time.sleep(60)#60
    ALERT_GALE1()
    time.sleep(10)#10
    DELETE_GALE1()
    time.sleep(50)#50


