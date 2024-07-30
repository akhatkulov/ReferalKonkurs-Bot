from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup,ReplyKeyboardRemove
from alch import get_channel
def admin_buttons():
    x = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Statistika", callback_data="stat")
    btn2 = InlineKeyboardButton(text="Xabar yuborish", callback_data="send")
    btn3 = InlineKeyboardButton(text="Kanallarni sozlash", callback_data="channels")
    x.add(btn1, btn2, btn3)
    return x


def channel_control():
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="➕Kanal qo'shish", callback_data="channel_add")
    btn2 = InlineKeyboardButton(text="➖Kanalni olib tashlash", callback_data="channel_del")
    x.add(btn1, btn2)
    return x

def join_key():
    keyboard = InlineKeyboardMarkup(row_width=1)
    x = get_channel()
    r = 1
    for i in x:
        keyboard.add(
            InlineKeyboardButton(f"〽️ {r}-kanal", url=f"https://t.me/{i}")
        )
        r += 1
    keyboard.add(InlineKeyboardButton('✅ Tasdiqlash', callback_data='/start'))
    return keyboard

def home_keys():
    x = ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    btn1 = KeyboardButton(text="🏆 Reyting")
    x.add(btn1)
    return x

def send_contact():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = KeyboardButton("📲 Telefon raqamni yuborish", request_contact=True)
    markup.add(button)
    return markup

def keyboard_rm():
    markup = ReplyKeyboardRemove()
    return markup

def start_go():
    x = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Boshlash 🚀",callback_data="start_go")
    x.add(btn1)
    return x