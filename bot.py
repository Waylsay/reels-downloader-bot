import telebot
bot = telebot.TeleBot("YOUR_BOT_TOKEN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я скачиваю reels, для скачивания пришли мне ссылку")

@bot.message_handler(func=lambda message: True)
def download_reels(message):
	if message.text.startswith('https://www.insta'):
		bot.send_message(message.chat.id, message.text[:12]+'dd'+ message.text[12:])
	else: bot.send_message(message.chat.id, "Некорректная ссылка")
bot.infinity_polling()
