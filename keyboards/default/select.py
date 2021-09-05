from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

brand_select = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить категорию автомобилей 🚗"),
        ],
        [
            KeyboardButton(text="Справка 📜"),
        ]

    ],
    resize_keyboard=True
)


beak_seleck_categori = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Я передумал добавлять категорию🤔"),
        ],

    ],
    resize_keyboard=True
)

beak_update_categori = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Я передумал обновлять категорию🤔"),
        ],

    ],
    resize_keyboard=True
)

home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить категорию автомобилей 🚗"),
        ],
        [
            KeyboardButton(text="Справка 📜"),
        ],
        [
            KeyboardButton(text="Обновить категорию автомобиля 🚙"),

        ],
        [
            KeyboardButton(text="Купить подписку Prime👑"),

        ]

    ],
    resize_keyboard=True
)
