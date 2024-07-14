import telebot
import requests


token = "7241613984:AAGjOWmogqvM1yD-q-VyQBe03ixzNT5FJQQ"
#توكنك
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
	
	bot.send_message(message.chat.id,'Send Your username ')
	
@bot.message_handler(func=lambda sen:True)
def sen(message):
	try:
		us = message.text
		url = f"https://www.instagram.com/{us}"
		rr = requests.get(url).text
		iid = rr.split('props":{"id":"')[1].split('"')[0]
		print(iid)
		
		bot.reply_to(message,f'user : {us}\nID : {iid}')
		
	except:
		bot.reply_to(message,'Baned username or not found')
		
		
print('Go Bot start')
bot.infinity_polling()