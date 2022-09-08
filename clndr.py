import calendar
import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import prefix, modules_help

dates = [['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
         ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']]


@Client.on_message(filters.command("clndr", prefix) & filters.me)
async def calc(_, message: Message):
    if len(message.command) > 2:
        if message.command[1].isdigit() and message.command[2].isdigit():
            date = calendar.month(int(message.command[1]), int(message.command[2]))
            for i in range(len(dates[0])):
                date = date.replace(dates[0][i], dates[1][i])
            await message.edit_text(f'```{date}```', parse_mode='markdown')
        else:
            await message.edit_text(f'Введите год цифрами')
    else:
        date = calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)
        for i in range(len(dates[0])):
            date = date.replace(dates[0][i], dates[1][i])
        await message.edit_text(f'```{date}```', parse_mode='markdown')


modules_help['clndr'] = {'clndr': 'year month | Calendar'}
