import telebot
import buttons

bot = telebot.TeleBot(token="6814553688:AAGcMe9pJPUkMvbq50oCg9EqQA40dy4tslQ")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bot.send_message(user_id, f"Привет {user_name}! Выберите операцию ниже:", reply_markup= buttons.button())

@bot.message_handler(content_types=["text"])
def convert(message):
    user_id = message.from_user.id
    user_text = message.text

    if user_text == "USD ➡️ UZS":
        bot.send_message(user_id, "Введите сумму для конвертации USD в UZS:")
        bot.register_next_step_handler(message, usd_to_uzs)
    elif user_text == "UZS ➡️ USD":
        bot.send_message(user_id, "Введите сумму для конвертации UZS в USD:")
        bot.register_next_step_handler(message, uzs_to_usd)
    else:
        bot.send_message(user_id, "Пожалуйста, выберите одну из предложенных операций.")

def usd_to_uzs(message):
    user_id = message.from_user.id
    kurs = 12000

    if message.text.isdigit():
        amount = int(message.text)
        result = amount * kurs
        bot.send_message(user_id, f"{amount} USD = {result} UZS")
    else:
        bot.send_message(user_id, "Пожалуйста, введите корректное число.")
        bot.register_next_step_handler(message, usd_to_uzs)

def uzs_to_usd(message):
    user_id = message.from_user.id
    kurs = 12500

    if message.text.isdigit():
        amount = int(message.text)
        result = amount / kurs
        bot.send_message(user_id, f"{amount} UZS = {result} USD")
    else:
        bot.send_message(user_id, "Пожалуйста, введите корректное число.")
        bot.register_next_step_handler(message, uzs_to_usd)

bot.infinity_polling()
