from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def oracle_keyboard():
    # Предсказание
    # Алкоголь: ДА/НЕТ - ЧТО
    # Секс ДА/НЕТ - ГДЕ - КАК - КУДА
    oracle_keyboard = InlineKeyboardMarkup(row_width=3)

    oracle_button = InlineKeyboardButton(text='Magic Ball', callback_data='oracle')
    sex_full = InlineKeyboardButton(text='Magic Sex Ball', callback_data='sex_full')
    sex_consent = InlineKeyboardButton(text='Sex Y|N', callback_data='oracle')
    sex_where = InlineKeyboardButton(text='Sex Where', callback_data='sex_where')
    sex_how = InlineKeyboardButton(text='Sex How', callback_data='sex_how')
    alcohol_consent = InlineKeyboardButton(text='Alco Y|N', callback_data='oracle')
    alcohol_choice = InlineKeyboardButton(text='Alco choice', callback_data='alcohol_choice')

    oracle_keyboard.add(oracle_button)
    oracle_keyboard.add(sex_full)
    oracle_keyboard.add(sex_consent, sex_where, sex_how)
    oracle_keyboard.add(alcohol_consent, alcohol_choice)
    return oracle_keyboard
