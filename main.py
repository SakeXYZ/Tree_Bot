import requests
import json
import os

from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
# Получение значений переменных окружения из файла .env

# Trello URL, IP, TOKEN
main_trello_end_point = os.getenv('URL')
trello_key = os.getenv('API_KEY')
trello_token = os.getenv('TOKEN')

# Trello ID - CARDS
application_list_id = os.getenv('ZM_ONE')
application_list_id_two = os.getenv('ZM_TWO')
application_list_id_tree = os.getenv('ZM_TREE')
application_list_id_four = os.getenv('ZM_FOUR')
application_list_id_five = os.getenv('ZM_FIVE')
application_list_id_six = os.getenv('ZM_SIX')
application_list_id_seven = os.getenv('ZM_SEVEN')
application_list_id_free_time = os.getenv('NO_CODE')

# Инициализация бота и диспетчера
bot = Bot(os.getenv('ZM_API'))
dp = Dispatcher(bot=bot)

# Создание клавиатуры с кнопкой "Инструкция"х
mainKeyBoard = ReplyKeyboardMarkup(resize_keyboard=True)
mainKeyBoard.add('ℹ️Инструкция')

try:
    # Обработчик команды /start
    @dp.message_handler(commands=['start'])
    async def process_start_command(msg: types.Message):
        # Пересылка сообщения пользователя в групповой чат
        # await msg.answer(msg.from_user.id)
        feedback = -1002060370973
        await bot.forward_message(feedback, msg.from_user.id, msg.message_id, msg.from_user.first_name)

        # await bot.send_message(msg.from_user.id, msg.chat.id)
        text_salam = """
    👋Добро пожаловать!🎉

    🤖Этот бот поможет вам обратиться в технический отдел.👨‍💻

    ❓Чтобы обратиться в технический отдел, просто задайте свой вопрос или проблему.💡

    📨Бот передаст ваше сообщение сотруднику технического отдел.⏳


    ℹ️ Инструкция ⬇️

    Пример запроса:

    #1 Технический отдел - Иванов Иван, Проблема с компьютером

    Внимание: 

    Отправляйте запросы в формате: [код][отдел][-][фамилия][имя][,][проблема] 📝

    Не отправляйте стикеры, голосовые сообщения и другие медиафайлы 🔇
                    """
        bot_picture = open("img/bot_pic.jpg", 'rb')
        await msg.answer_photo(photo=bot_picture, caption=text_salam, reply_markup=mainKeyBoard)
except Exception as startErr:
    # Обработка ошибки, если возникает проблема при выполнении команды /start
    print(f'Ошибка при попытке запустить бота: Ошибка: {startErr}')

try:
    # Обработчик нажатия кнопки "ℹ️Инструкция"
    @dp.message_handler(text='ℹ️Инструкция')
    async def cmd_instructions(msg: types.Message):
        logo = open('img/Instruction.jpg', 'rb')
        info_text = """

Правила использования бота:

Отправляйте запросы в формате: [код отдела][отдел][-][фамилия][имя][,][проблема] 📝, как указано в примере.

Используйте коды отделов: 

#1 Офис БиоМир -
#2 Бухгалтерия БМ - 
#3 ИП Закирова -
#4 Склад -
#5 Дени Сак Элим - 
#6 Здоровый Мир -

Пример запроса:

#1 Офис БиоМир - Петр, проблема с интернетом

#2 Бухгалтерия БМ - Елена, ошибки при работе с принтером

#3 ИП Закирова - Анна, нет подключения к сети

#4 Склад - Дмитрий, пропал звук с камер видеонаблюдении

#5 Дени Сак Элим - Ольга, требуется техническая поддержка

#6 Здоровый Мир - Алексей, требуется просмотр с камер видеонаблюдении

Не отправляйте стикеры, голосовые и другие медиафайлы 🔇.

Точно повторяйте формат примера.

Соблюдайте четкость и ясность при описании проблемы.

Нарушения правил могут привести к ограничению доступа к боту.
                    """
        await msg.answer_photo(photo=logo, caption=info_text)
except Exception as InfoErr:
    # Обработка ошибки, если возникает проблема при нажатии кнопки "Инструкция"
    print(f"Ошибка {InfoErr} при нажатии кнопки 'Инструкция' ")

try:
    # Функция для создания карточки Trello
    def create_trello_card(card_name, card_desc, number_one):

        try:
            card_name = card_name.split()
            print(card_name)
            create_card_end_point = main_trello_end_point + 'cards'
            json_object = {"key": trello_key,
                           "token": trello_token,
                           "idList": number_one,
                           "name": ' '.join(card_name),
                           "desc": card_desc}
            new_card = requests.post(create_card_end_point, json=json_object)
            return json.loads(new_card.text)
        except KeyError as key_err:
            print(f'Неизвестная ошибка {key_err}')
        # Отправка запроса на создание карточки в Trello

except Exception as SendToTrelloErr:
    # Обработка ошибки, если возникает проблема при отправке запроса в Trello
    print(f"Ошибка {SendToTrelloErr} при отправке запроса в Trello")


def text_process(list_accept):
    try:
        list_id_mapping = {
            '#1': application_list_id,
            '#2': application_list_id_two,
            '#3': application_list_id_tree,
            '#4': application_list_id_four,
            '#5': application_list_id_five,
            '#6': application_list_id_six,
            '#7': application_list_id_seven,
        }
        change_list = ' '.join(list_accept)
        change_2 = change_list.split('-')
        change_list = change_2[0].split()

        print(list_accept[0:2], list_accept[2::])
        print(f"{change_list[0]} Change list")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y")
        tm_string = now.strftime('%H:%M:%S')
        # Создание карточки Trello на основе текста сообщения пользователя
        print(create_trello_card(' '.join(change_list),
                                 ''.join(change_2[1]) + '\n\nДата:' + dt_string + f'\nВремя:{tm_string}',
                                 list_id_mapping[change_list[0]]))
    except KeyError as key_error:
        change_list = ' '.join(list_accept)
        change_2 = change_list.split('-')
        change_list = change_2[0].split()

        print(list_accept[0:2], list_accept[2::])
        print(f"{change_list[0]} Change list")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y")
        tm_string = now.strftime('%H:%M:%S')
        # Создание карточки Trello на основе текста сообщения пользователя
        print(create_trello_card(' '.join(change_list),
                                 ''.join(change_2[1]) + '\n\nДата:' + dt_string + f'\nВремя:{tm_string}',
                                 application_list_id_free_time))
        print(f"Ошибка: {key_error}")


try:
    # Обработчик всех остальных сообщений от пользователя 
    @dp.message_handler()
    async def echo_message(msg: types.Message):
        # Пересылка сообщения пользователя в групповой чат
        feedback = -1002060370973
        await bot.forward_message(feedback, msg.from_user.id, msg.message_id, msg.from_user.first_name)
        print(msg.text.split(' '))
        # Отправка видео и уведомления о времени обработки заявки
        await bot.send_video(msg.chat.id, open('img/Gif_ask.gif', 'rb'),
                             caption="🤖Ваша заявка будет обработана в течение 15 минут!!!🤖")
        list_accept = []
        for i in msg.text.split():
            list_accept.append(i)
        text_process(list_accept)
except Exception as ind_err:
    print(f"Ошибка при отправке на обработке")

if __name__ == "__main__":
    executor.start_polling(dp)
