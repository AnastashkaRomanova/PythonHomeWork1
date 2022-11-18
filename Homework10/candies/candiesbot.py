from aiogram import Bot,Dispatcher
from aiogram import types
from keyboard import candies_keyboard
import random
import asyncio
token = "***"
bot = Bot(token)
dp = Dispatcher(bot)

candies = 101

async def on_startup(_):
    print('I see you!')


def win(candies):
    if candies<= 0:
        return True
    else:
        return False

def comp_take():
    return random.randint(1, 29)
    

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет!\n Поиграй со мной!Нажимай: /game")

@dp.message_handler(commands=["new_game"])
async def newgame(message:types.Message):
    global candies
    #candies = 101
    await message.answer(
        'Правила игры:\n Ходим по очереди, за один ход можно взять от 1 до 28 конфет. Изначально есть 101 конфета.\n '
        'Если твой ход будет последним, ты забираешь конфеты себе и ты победишь! Твой ход', reply_markup=candies_keyboard)


@dp.message_handler(commands=["game"])
async def cmd_game_start(message: types.Message):
    await message.answer('Правила игры:\n Ходим по очереди, за один ход можно взять от 1 до 28 конфет. Изначально есть 101 конфета.\n '
        'Если твой ход будет последним, ты забираешь конфеты себе и ты победишь! Твой ход', reply_markup=candies_keyboard)

@dp.callback_query_handler()
async def process_callback(callback: types.CallbackQuery):
    global candies
    data = callback.data
    if win(candies):
        await callback.answer('Я победил\nЗахочешь заново набери /new_game')
        return 1
    await callback.answer(f'Ты взял {data} конфет')
    candies = candies - int(data)
    if candies <= 0 :
        await callback.message.answer(f'ты победил \nЗахочешь заново набери /new_game')
        return 1
    else:
        await callback.message.answer(f'осталось {candies} конфет.Бери теперь ты!')
    comptake=comp_take()
    candies = candies - comptake
    if win(candies):
        await callback.message.answer('я победил !!! \nЗахочешь заново набери /new_game')
    else:
        await callback.message.answer(f'я взял себе {comptake}, осталось {candies} конфет')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())     