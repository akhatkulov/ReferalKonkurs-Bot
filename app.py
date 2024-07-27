import telebot
from telegraph import upload_file
from io import BytesIO

from alch import User, create_user, get_step, put_step, put_ball, get_ball, user_count, get_all_user, \
    get_channel, put_channel, get_channel_with_id, delete_channel,get_list,get_name,get_phone,put_name,put_phone

from helper.buttons import admin_buttons,channel_control,join_key,home_keys,send_contact,keyboard_rm
from helper.functions import mini_decrypt, mini_crypt,create_excel_file
bot = telebot.TeleBot('7223905979:AAGRsNXcFV5tNLzxXww_LmXEkOGbllL6fUM', parse_mode="html")


admin_id = 6521895096

def join(user_id):
    try:
        xx = get_channel()
        r = 0
        for i in xx:
            res = bot.get_chat_member(f"@{i}", user_id)
            x = ['member', 'creator', 'administrator']
            if res.status in x:
                r += 1
        if r != len(xx):
            bot.send_message(user_id,
                             "<b>👋 Assalomu alaykum Botni ishga tushurish uchun kanallarga a'zo bo'ling va a'zolikni tekshirish buyrug'ini bosing.</b>",
                             parse_mode='html', reply_markup=join_key())
            return False
        else:
            return True
    except Exception as e:
        bot.send_message(chat_id=admin_id, text=f"Kanalga bot admin qilinmagan yoki xato: {str(e)}")
        return True


@bot.message_handler(commands=['start'])
def start(message):
    

    if message.text == "/start" and join(message.chat.id):
        bot.send_message(message.chat.id,
                             f"<b>Salom, {message.chat.first_name} botimizga xush kelibsiz</b>\n🔗Taklif linki:\nhttps://t.me/Nasibadjumayevabot?start={mini_crypt(str(message.chat.id))}",
                             parse_mode='html',reply_markup=home_keys())
        try:
            create_user(cid=message.chat.id,name=message.chat.first_name)
        except Exception as e:
            print(f"Error creating user: {str(e)}")
        put_step(cid=message.chat.id, step="!!!")
        if get_name(cid=message.chat.id) == "Qoqindiq":
            bot.send_message(chat_id=message.chat.id,text="Ismingiz yuboring")
            put_step(cid=message.chat.id,step="name")
        

    if "/start" in message.text and len(message.text) > 6:
        adder = list(message.text.split())
        x = adder[1]
        res = mini_decrypt(x)
        put_step(cid=message.chat.id, step="!!!")
        print(res,get_all_user())
        if message.chat.id not in get_all_user(): 
            ball = get_ball(cid=res)
            ball += 1
            put_ball(cid=res,ball=ball)
            bot.send_message(chat_id=res,text="1 ball qo'shildi")
            try:
                create_user(cid=message.chat.id,name=message.chat.first_name)
            except Exception as e:
                print(f"Error creating user: {str(e)}")

        if res == message.chat.id:
            bot.send_message(chat_id=res,text="O'zingizni taklif qila olmaysizku, axir!")
        
        if get_name(cid=message.chat.id) == "Qoqindiq":
            bot.send_message(chat_id=message.chat.id,text="Ismingiz yuboring")
            put_step(cid=message.chat.id,step="name")
        else:
            bot.send_message(message.chat.id,
                             f"<b>Salom, {message.chat.first_name} botimizga xush kelibsiz</b>\n🔗Taklif linki:\nhttps://t.me/Nasibadjumayevabot?start={mini_crypt(str(message.chat.id))}",
                             parse_mode='html',reply_markup=home_keys())


@bot.message_handler(content_types=['text'])
def more(message):
    if message.text == "/send" and message.chat.id == admin_id:
        try:
            with open("data/data.xlsx", 'rb') as file:
                bot.send_document(message.chat.id, file)
        except:
            bot.send_message(chat_id=message.chat.id,text="Fayl mavjud emas!")
    if message.text == "🏆 Reyting":
        bot.send_message(chat_id=message.chat.id,text=get_list(target=message.chat.id),parse_mode="html")
    
    if message.text == "/admin" and message.chat.id == admin_id:
        bot.send_message(chat_id=admin_id, text="Salom, Admin", reply_markup=admin_buttons())
        put_step(cid=message.chat.id, step="!!!")

    if get_step(message.chat.id) == "name":
        put_name(cid=message.chat.id,name=message.text)
        bot.send_message(chat_id=message.chat.id,text="Raqamingizni yuboring",reply_markup=send_contact())
        put_step(cid=message.chat.id, step="phone")
    if get_step(message.chat.id) == "channel_del" and message.text != "/start" and message.text != "/admin":
        x = int(message.text)
        if delete_channel(ch_id=x):
            bot.send_message(chat_id=message.chat.id, text="Kanal olib tashlandi")
            put_step(cid=message.chat.id, step="!!!")
        else:
            bot.send_message(chat_id=message.chat.id, text="Xatolik! IDni to'g'ri kiritdingizmi tekshiring!")

    if get_step(message.chat.id) == "add_channel" and message.text != "/start" and message.text != "/admin":
        if put_channel(message.text):
            bot.send_message(chat_id=message.chat.id, text=f"{message.text} kanali qabul qilindi!")
            put_step(cid=int(admin_id), step="!!!")
        else:
            bot.send_message(chat_id=message.chat.id,
                             text="Xatolik! Bu kanal oldin qo'shilgan bo'lishi mumkin yoki boshqa xatolik, iltimos tekshiring")
            put_step(cid=int(admin_id), step="!!!")
    
    if get_step(message.chat.id) == 'send':
        text = message.text
        mid = message.id
        bot.send_message(chat_id=message.chat.id, text="Xabar yuborish boshlandi")
        try:
            for i in get_all_user():
                try:
                    bot.forward_message(chat_id=i, from_chat_id=admin_id, message_id=mid)
                except Exception as e:
                    print(f"Error sending message to user {i}: {str(e)}")
            bot.send_message(chat_id=message.chat.id, text="Tarqatish yakunlandi")
            put_step(cid=int(admin_id), step="!!!")
        except Exception as e:
            bot.send_message(chat_id=message.chat.id, text=f"Xabar yuborishda muammo bo'ldi: {str(e)}")

@bot.message_handler(content_types=['contact'])
def get_contacts(message):
    if get_step(message.chat.id):
        contact = message.contact
        put_phone(cid=message.chat.id,phone=contact.phone_number)
        bot.send_message(message.chat.id, f"""<b>Salom, {get_name(cid=message.chat.id)} botimizga xush kelibsiz</b>\n🔗Taklif linki:\nhttps://t.me/Nasibadjumayevabot?start={mini_crypt(str(message.chat.id))}""",reply_markup=home_keys())    
        data = [
            [get_name(cid=message.chat.id), get_phone(cid=message.chat.id)]
        ]
        create_excel_file(filename="data/data.xlsx",data=data,)
        
        put_step(cid=message.chat.id,step="!!!")
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):  
    if call.data == "/start" and join(call.message.chat.id):
        bot.send_message(call.message.chat.id, f"""<b>Salom, {call.message.chat.first_name} botimizga xush kelibsiz</b>\n🔗Taklif linki:\nhttps://t.me/Nasibadjumayevabot?start={mini_crypt(str(call.message.chat.id))}""",reply_markup=home_keys())  
    if call.data == "stat" and str(call.message.chat.id) == str(admin_id):
        bot.send_message(chat_id=call.message.chat.id, text=f"Foydalanuvchilar soni: {user_count()}")
    if call.data == "send" and str(call.message.chat.id) == str(admin_id):
        put_step(cid=call.message.chat.id, step="send")
        bot.send_message(chat_id=call.message.chat.id, text="Forward xabaringizni yuboring")
    if call.data == "channels" and str(call.message.chat.id) == str(admin_id):
        r = get_channel_with_id()
        bot.send_message(chat_id=call.message.chat.id, text=f"Kanallar ro'yxati:{r}", reply_markup=channel_control())
    if call.data == "channel_add" and str(call.message.chat.id) == str(admin_id):
        put_step(cid=call.message.chat.id, step="add_channel")
        bot.send_message(chat_id=call.message.chat.id, text="Kanali linkini yuboring! bekor qilish uchun /start !")
    if call.data == "channel_del" and str(call.message.chat.id) == str(admin_id):
        put_step(cid=call.message.chat.id, step="channel_del")
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"{get_channel_with_id()}\n⚠️O'chirmoqchi bo'lgan kanalingiz IDsini bering, bekor qilish uchun /start yoki /admin deng!")

if __name__ == '__main__':
    print(bot.get_me())
    bot.polling(none_stop=True)
