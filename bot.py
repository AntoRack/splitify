import telebot
import time

TOKEN = '766072158:AAHbGg4FynSbXDQAqLkdTfouHkjhMKvh--k'

amount=0
person=0
credit={}
debit={}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['reset'])
def send_reset(message):
	amount=0
	bot.reply_to(message, "'A man remember his debts'")

@bot.message_handler(commands=['join'])
def add(message):
	cid = message.chat.id
	credit[cid] = 0
	debit[cid] = 0
	person+=1
	bot.reply_to(message, "Welcome"+ message.from_user)

@bot.message_handler(commands=['summary'])
def summary(message):
	str= "Amount:"+amount+"	person:"+person+" credit:"+credit+"	debit:"+debit
	bot.reply_to(message,str)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "wiki are for noob")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(commands=[''])
def send_welcome(message):
	person+=1
	bot.reply_to(message, "")

bot.polling()