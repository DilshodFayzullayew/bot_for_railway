from aiogram import Bot, Dispatcher, types, executor
import logging
import base
import os
from user import User
from aiogram.types import ReplyKeyboardMarkup,InputFile, CallbackQuery, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import asyncio


API_KEY = "7009118329:AAHbY5XKpCSJ2dxZSrSUiQWscWgTg4uJ8q0"
logging.basicConfig(level=logging.INFO)
bot = Bot(API_KEY)
dp = Dispatcher(bot)


questions = {
        "Manyovr ishlarini kim boshqaradi?":{
            "options":["Mashinist","Yordamchi","Dispatcher","Chilangar"],
            "answer":"1-javob"
        },
        "Yo‘l belgilarning asosiy vazifasi nima?": {
            "options": ["Harakat havfsizligi", "Bilish uchun", "To`g`ri boshqarish", "Poyezd manyovri uchun"],
            "answer": "2-javob"
        },
        "Temir yo`l svetoforining qaysi rangi taqiqlovchi ishorani bildiradi?": {
            "options": ["qizil", "ko`k", "qora", "yashil"],
            "answer": "3-javob"
        },
        "Xavfli yuklar bilan manyovr ishlari qanday tezlikda bajariladi?": {
            "options": ["12 km/s", "15 km/s", "15 km/s", "4 km/s"],
            "answer": "4-javob"
        },
        "Teplovoz vagonlarga qanday tezlikda ulanishi mumkin?": {
            "options": ["14 km/s", "21 km/s", "3 km/s", "4 km/s"],
            "answer": "4-javob"
        },
       "Qanday lokomotiv itaruvchi xisoblanadi?": {
            "options": ["Teplovoz", "Elektrovoz", "Barchasi", "Xech qaysisi"],
            "answer": "4-javob"
        }

    }

questions_for_AI = {
        "Tormoz boshmog‘ini o‘rnatish qoidalari nech turi bor?":{
            "options":["|1 ta","|2 ta","|3 ta","|4 ta"],
            "answer":"1-javob"
        },
        "Manyovrlarni boshqarishda asosiy aloqa vositasi nima?": {
            "options": ["|Harakat havfsizligi", "|Ratsya", "|To`g`ri boshqarish", "|Teplovoz"],
            "answer": "2-javob"
        },
        "Temir yo‘lning normal kengligi?": {
            "options": ["|1050", "|1080", "|1070", "|1060"],
            "answer": "3-javob"
        },
        "Teplovozni vagonlardan uzish va ulash qoidalari necha turi mavjud?": {
            "options": ["|2 ta", "|5 ta", "|1 ta", "|4 ta"],
            "answer": "4-javob"
        },
        "Vagon raqami nechta sondan iborat bo‘ladi?": {
            "options": ["|4 ta", "|1 ta", "|3 ta", "|5 ta"],
            "answer": "4-javob"
        },
       "Yuk poezdining orqa qismini belgilanishi.": {
            "options": ["|Teplovoz", "|Elektrovoz", "|Barchasi", "|Xech qaysisi"],
            "answer": "4-javob"
        }

    }

def admin_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    statistika = KeyboardButton("Ishchilar 👨‍🔧")
    movies = KeyboardButton("Oylik maosh 💴")
    reklama = KeyboardButton("Intizomiy jazolar ⚠️")
    add_chanell = KeyboardButton("Qilingan ishlar 🏁")
    done = KeyboardButton("Darsliklar 📚")
    test = KeyboardButton("Test to`plamlari 📓")
    return btn.add(statistika, movies, reklama, add_chanell,done, test)

def user_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    statistika = KeyboardButton("Ma`lumotlarim ℹ️")
    movies = KeyboardButton("Oylik maoshlarim 💴")
    add_chanell = KeyboardButton("Qilgan ishlarim 🏁")
    done = KeyboardButton("Darsliklar 📚")
    daraja = KeyboardButton("Darajamni oshirish ⬆️")
    exam = KeyboardButton("Imtihon topshirish ✍️")
    exam_res = KeyboardButton("Imtihon javoblari(SI) 🤖")
    savol = KeyboardButton("Savol yo`llash 📨")
    return btn.add(statistika, movies, add_chanell,done, daraja,exam,exam_res,savol)




def user_inline_btn(user_telegram_id, path):
    keyboard = InlineKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    res = User()
    response = res.get_file(user_telegram_id, path)
    for data in response:
        button = InlineKeyboardButton(data, callback_data=f'button_precced_{data}')
        keyboard.insert(button)
    return keyboard


def user_inline_btn_for_work(user_telegram_id, path):
    keyboard = InlineKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    res = User()
    response = res.get_file(user_telegram_id, path)
    for data in response:
        button = InlineKeyboardButton(data, callback_data=f'button_preccedd_{data}', pay=False)
        keyboard.insert(button)
    return keyboard


def inbtn_for_AI():
    keyboard = InlineKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("Ha, o`rganaman!", callback_data=f'_data_{1}')
    button2 = InlineKeyboardButton("Yo`q, keyinroq!", callback_data=f'_data_{2}')
    keyboard.add(button1, button2)
    return keyboard


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    await message.answer("Iltimos table raqam va parolingizni birgalikda kiriting!\n"
                         "-------------------------\n"
                         "tabel raqam | parol\n"
                         "1234               1234")

## admin panel
@dp.message_handler(text="Ishchilar 👨‍🔧")
async def worker(message: types.Message):
    await message.answer(text = "worker")

@dp.message_handler(text="Oylik maosh 💴")
async def salary(message: types.Message):
    await message.answer(text = "salary")

@dp.message_handler(text="Intizomiy jazolar ⚠️")
async def violation(message: types.Message):
    await message.answer(text = "jazolar")

@dp.message_handler(text="Qilingan ishlar 🏁")
async def done_jobs(message: types.Message):
    await message.answer(text = "done")

@dp.message_handler(text="Darsliklarr 📚")
async def cook_books(message: types.Message):
    await message.answer(text = "dars")

@dp.message_handler(text="Test toplamlari 📓")
async def test(message: types.Message):
    await message.answer(text = "test")

### user panel
@dp.message_handler(text="Ma`lumotlarim ℹ️")
async def salary(message: types.Message):
    user_telegram_id = message.from_user.id
    res = User()
    result = res.get_information(user_telegram_id)
    await message.answer(f"──────── ⋆⋅☆⋅⋆ ────────\n"
                         f"👤 F.I.SH: {result.full_name}\n"
                         f"🔢 Tabel raqami: {result.table_number}\n"
                         f"🏢 Ish joyi: {result.sex_number}\n"
                         f"⬆️ Lavozimi: {result.level}\n"
                         f"⏰ Ish tajribasi: {result.year_of_work}\n"
                         f"📄 Ma`lumoti: {result.degree}\n"
                         f"📑 INN raqami: {result.inn_number}\n"
                         f"📰 passport raqami: {result.passport_number}\n"
                         f"────────────────────\n"
                         f"Ko`rikdan o`tilgan sana: 23.08.2023\n"
                         f"Keyingi ko`rik: 23.08.2024\n"
                         f"────────────────────\n"
                         f"Moddiy yordam: Siz hech qanday moddiy yordam olmagansiz!\n"
                         f"Intizomiy jazolar: Sizning intizomiy jazolarinigiz yo`q!\n"
                         f"Mehnat ta`tili: Siz bu yil mehnat tatiliga chiqmagansiz!\n"
                         f"──────── ⋆⋅☆⋅⋆ ────────")

###salary
@dp.message_handler(text="Oylik maoshlarim 💴")
async def violation(message: types.Message):
    user_tg_id = message.from_user.id
    btns = user_inline_btn(user_tg_id, "Karashok")
    await message.answer("Iltimos kerakli sanani tanlang!", reply_markup=btns)

@dp.callback_query_handler(lambda c: c.data.startswith('button_precced_'))
async def hello_callback(callback_query: CallbackQuery):
    pressed_button = callback_query.data.replace('button_precced_', '')
    res = User()
    salary = res.get_salary(pressed_button,"Karashok")
    await bot.send_message(callback_query.from_user.id,f"──────── ⋆⋅☆⋅⋆ ────────\n"
                                                            f"F.I.Sh : {salary.toliq_ismi}\n"
                                                       f"Tabel raqami : {salary.tabel_number}\n"
                                                       f"Ish joyi : {salary.sex}\n"
                                                       f"Lavozimi : {salary.Lavozim}\n"
                                                       f"ish haqi : {salary.ish_haqi}\n"
                                                       f"247 : {salary._247}\n"
                                                       f"013 :{salary._013}\n"
                                                       f"001 : {salary._001}\n"
                                                       f"Jami yig`ilgan : {salary.jami_yigilgan}\n"
                                                       f"────────────────────\n"
                                                       f"882 : {salary._882}\n"
                                                       f"902 : {salary._902}\n"
                                                       f"879 : {salary._879}\n"
                                                       f"887 : {salary._877}\n"
                                                       f"Jami ushlangan : {salary.jami_ushlangan}\n"
                                                       f"────────────────────\n"
                                                       f"12 887 : {salary._12_887}\n"
                                                       f"Plastik : {salary.plastik}")
    await bot.delete_message(callback_query.message.chat.id,callback_query.message.message_id)

##salary

## workes
@dp.message_handler(text="Qilgan ishlarim 🏁")
async def cook_books(message: types.Message):
    user_tg_id = message.from_user.id
    btns = user_inline_btn_for_work(user_tg_id, "BajarilganIshlar")
    await message.answer("Iltimos kerakli sanani tanlang!", reply_markup=btns)

@dp.callback_query_handler(lambda c: c.data.startswith('button_preccedd_'))
async def hello_callback(callback_query: CallbackQuery):
    pressed_button = callback_query.data.replace('button_preccedd_', '')
    res = User()
    salary = res.get_salary(pressed_button,"BajarilganIshlar")
    await bot.send_message(callback_query.from_user.id, f"──────── ⋆⋅☆⋅⋆ ────────\n"
                                                        f"Tabel raqami: {salary.tabel_number}\n"
                                                        f"Ma`sul shaxs: {salary.masul_shaxs}\n"
                                                        f"Qabul qilgan shaxs: {salary.tekshirdi}\n"
                                                        f"────────────────\n"
                                                        f"Qilgan ishingiz: {salary.type}\n"
                                                        f"Sana: 2024.02.29\n"
                                                        f"Ta`mirlangan poyezd raqami: {salary.poyezd}\n"
                                                        f"##################\n"
                                                        f"Qilgan ishingiz: mator izolyatsiyasini almashtirdi\n"
                                                        f"Sana: 2024.03.01\n"
                                                        f"Tamirlangan poyezd raqami: 1090\n"
                                                        f"###############\n"
                                                        f"Qilgan ishingiz: Kompressorga moy quydi\n"
                                                        f"Sana: 2024.03.08\n"
                                                        f"Tamirlangan poyezd raqami: 3050")
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
## workes
## dars
@dp.message_handler(text="Darsliklar 📚")
async def test(message: types.Message):
    pdf_file = InputFile("C:\\Users\\Hp\\Desktop\\admin\\Darsliklar\\6-sex Darsliklari.pdf")
    await bot.send_document(message.chat.id,document=pdf_file)
    await message.answer("Iltimos bu kitobni imtihongacha yaxshilab o`qib chiqing!")
## dars
## daraja
question_to_message = {}


async def ask_questions(message: types.Message):
    for question_text, question_data in questions.items():
        options = question_data["options"]
        correct_answer = question_data["answer"]
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        for option in options:
            keyboard_markup.add(InlineKeyboardButton(option, callback_data=option))

        question_message = await message.answer(question_text, reply_markup=keyboard_markup)
        question_to_message[question_message.message_id] = question_text
        await asyncio.sleep(10)





@dp.message_handler(text="Darajamni oshirish ⬆️")
async def start_test(message: types.Message):
    await message.answer("Tayyormisiz, savollarga javob bering!")
    await ask_questions(message)
    await message.answer("Javoblarini masteringizga yuboramiz!")


@dp.callback_query_handler()
async def check_answer(callback_query: types.CallbackQuery):
    user_answer = callback_query.data
    message_id = callback_query.message.message_id
    question_text = question_to_message.get(message_id)
    if user_answer == "_data_1":

        await bot.send_message(callback_query.from_user.id,"Iltimos kuting, bu qismi ishlab chiqish jarayonida!")
    if user_answer == "_data_2":
        await bot.send_message(callback_query.message.chat.id,"Ko`proq bilim oling, siz bizning korhonaga keraksiz!")
    if not question_text:
        return

    correct_answer = True

    if user_answer == correct_answer:
        await callback_query.answer("Yuklanmoqda!")
    else:
        await callback_query.answer("Yuklanmoqda!")

    # Remove the question message
    await bot.delete_message(callback_query.message.chat.id, message_id)

## daraja

## imtihon
question_to_message = {}


async def ask_questionss(message: types.Message):
    for question_text, question_data in questions_for_AI.items():
        options = question_data["options"]
        correct_answer = question_data["answer"]
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        for option in options:
            keyboard_markup.add(InlineKeyboardButton(option, callback_data=option))

        question_message = await message.answer(question_text, reply_markup=keyboard_markup)
        question_to_message[question_message.message_id] = question_text
        await asyncio.sleep(10)




@dp.message_handler(text="Imtihon topshirish ✍️")
async def start_test(message: types.Message):
    with open("D:\\lessonbot\\number.txt", "w") as file:
        file.write(str(1))
    await ask_questionss(message)
    await message.answer("Javoblarini Sun`iy intelekt orqali bilib oling!")


@dp.callback_query_handler(lambda c: c.data.startswith('|'))
async def check_answer(callback_query: types.CallbackQuery):
    user_answer = callback_query.data
    message_id = callback_query.message.message_id
    question_text = question_to_message.get(message_id)
    if not question_text:
        # This callback query does not belong to a question message
        return

    correct_answer = questions[question_text]["answer"]

    if user_answer == correct_answer:
        await callback_query.answer("Yuklanmoqda!")
    else:
        await callback_query.answer("Yuklanmoqda!")

    # Remove the question message
    await bot.delete_message(callback_query.message.chat.id, message_id)


### SI



@dp.message_handler(text="Imtihon javoblari(SI) 🤖")
async def test(message: types.Message):
    res = User()
    count = message.from_user.id
    with open("D:\\lessonbot\\number.txt", "r") as file:
        lines = file.readlines()
    exists = False
    for line in lines:
        if "1" in line:
            exists = True
            break
    if not exists:
        await message.answer("Suniy intelekt sizni baholashi uchun siz imtihon topshiroshingiz kerak!")
    if count % 2 == 0 and exists:
        fraph = res.graph([1, 2, 3, 4, 5], [2, 3, 5, 4, 1])
        await bot.send_photo(chat_id=message.chat.id, photo=types.InputFile(fraph, filename='graph.png'))
        btns = inbtn_for_AI()

        await message.answer("Sizda koproq hodovoy qismida bilim va ko`nikmalar ko`proq ekan, "
                             "keling siz bilan mening yordamimda boshqa qisimlarini ham birga o`rgansak",
                             reply_markup=btns)
    if count % 2 == 1 and exists:
        fraph = res.graph([1, 3,4 , 5, 6], [3, 3, 2, 4, 5])
        await bot.send_photo(chat_id=message.chat.id, photo=types.InputFile(fraph, filename='graph.png'))
        btns = inbtn_for_AI()

        await message.answer("Sizda barcha kerakli nazariyalarga egasiz, "
                             "lekin siz yanada ko`proq bilim olishingiz kerak!"
                             "Shu boisdan Suniy Intelekt sizga ko`proq bilim va ko`nikmalar o`rganishingizga yordam bermoqchi!",
                             reply_markup=btns)




@dp.callback_query_handler(lambda c: c.data.startswith('_'))
async def check_answer(callback_query: types.CallbackQuery):
    await callback_query.answer("Hello")

## savol






## savol

## SI

@dp.message_handler()
async def process_user_input(message: types.Message):
    user_input_list = message.text
    user_splited = user_input_list.split(" ")
    try:
        user_id = message.from_user.id
        response = base.is_user_exist(user_input_list, user_id)
        if response == "notTrue":
            await message.answer("Iltimos table raqam va parolingizni birgalikda kiriting!")
        if response == "userNotexists":
            await message.answer(f"Bunday tabel raqamli hodim topilmadi: {user_splited[0]} !")
        if response == "passanduser":
            await message.answer("Iltimos parolingizni to`g`ri kiriting!")
        if response =="admpass":
            await message.answer("Admin iltimos parolingizni to`g`ri kiriting!")
        if response == "admin":
            file_path = os.environ['appdata']
            index = file_path.find('Hp')
            substring = file_path[:index + 2]
            substring + "\\Desktop\\admin\\adminPassword"
            if not os.path.exists(substring):
                os.makedirs(substring + "\\Desktop\\admin\\adminPassword")
                with open(substring + "\\Desktop\\admin\\adminPassword\\admin.txt", "w") as file:
                    file.write("32134 32134")
            res = admin_btn()
            await message.answer("Salom admin",reply_markup=res)

        if response == "user":
            res = user_btn()
            await message.answer("Assalomu alekom! Hurmatli ishchi!", reply_markup=res)

    except Exception as e:
        print(e)
        await message.answer("Iltimos boshqatan takrorlab korin!")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)