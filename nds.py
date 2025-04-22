import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.enums import ParseMode

BOT_TOKEN = "7988149741:AAEVJ1b07cmBsVTWDTlGmLJDh7-j_HOEfv0"  # Замени на свой токен

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Функция форматирования чисел (например, 1000000 → 1 000 000)
def format_number(number):
    try:
        return f"{number:,.0f}".replace(",", " ").replace(".", ",")
    except:
        return str(number)

@dp.message(F.text)
async def handle_number(message: Message):
    try:
        clean_text = message.text.replace(" ", "").replace(",", ".")
        number = float(clean_text)

        step1 = 12 / 112 * number
        result = step1
        text = (
            f"<b>Сумма:</b> <b>{format_number(number)}</b>\n"
            f"<b>НДС (12%)</b> от {format_number(number)} = (12 / 112) * {format_number(number)} = <b>{format_number(result)}</b>\n"
            f"<b>Сумма без НДС</b> = {format_number(number)} - {format_number(result)} = <b>{format_number(number - result)}</b>"
        )

        await message.answer(text, parse_mode=ParseMode.HTML)

    except ValueError:
        await message.answer("Пожалуйста, введите корректное число.\nНапример: 1000 или 1500,5")

@dp.message()
async def start_message(message: Message):
    await message.answer("Введите сумму для расчета НДС (12%):")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

