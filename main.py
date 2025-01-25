from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

API_TOKEN = '8133327917:AAFqI7wXixOD2La2TNL7qXrMKSJv6rUwf_I'

main_menu = ReplyKeyboardMarkup([["Еда", "Напитки", "Десерты"]], resize_keyboard=True)
food_menu = ReplyKeyboardMarkup([["Хот-доги", "Бургеры", "Пицца"], ["Назад в главное меню"]], resize_keyboard=True)
hot_dogs_menu = ReplyKeyboardMarkup([["Классический хот-дог", "Хот-дог с сыром", "Хот-дог с беконом"], ["Назад в меню еды"]], resize_keyboard=True)
drinks_menu = ReplyKeyboardMarkup([["Вода", "Кола", "Чай", "Кофе"], ["Назад в главное меню"]], resize_keyboard=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Добро пожаловать в кафе! Выберите категорию:")

def handle_menu(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "Еда":
        update.message.reply_text("Выберите категорию еды:", reply_markup=food_menu)
    elif text == "Хот-доги":
        update.message.reply_text("Выберите хот-дог:", reply_markup=hot_dogs_menu)
    elif text in ["Классический хот-дог", "Хот-дог с сыром", "Хот-дог с беконом"]:
        update.message.reply_text("Хотите выбрать напиток?", reply_markup=drinks_menu)
    elif text == "Напитки":
        update.message.reply_text("Выберите напиток:", reply_markup=drinks_menu)
    elif text == "Десерты":
        update.message.reply_text("Пока десертов нет. Возвращайтесь позже!", reply_markup=main_menu)
    elif text in ["Вода", "Кола", "Чай", "Кофе"]:
        update.message.reply_text(f"Вы выбрали: {text}. Приятного аппетита!", reply_markup=main_menu)
    elif text == "Назад в главное меню":
        update.message.reply_text("Возврат в главное меню:", reply_markup=main_menu)
    elif text == "Назад в меню еды":
        update.message.reply_text("Возврат в меню еды:", reply_markup=food_menu)
    else:
        update.message.reply_text("Извините, я не понимаю эту команду. Попробуйте снова.", reply_markup=main_menu)

def main():
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))  
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))  

    application.run_polling()

if __name__ == '__main__':
    main()
