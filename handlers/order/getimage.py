import aiohttp
import os
from aiogram import types
from tempfile import NamedTemporaryFile

async def download_and_send_image(image_urls: list, caption: str, message: types.Message):
    media_files = ['a']

    # async with aiohttp.ClientSession() as session:
    #     for idx, image_url in enumerate(image_urls):
    #         try:
    #             async with session.get(image_url) as resp:
    #                 if resp.status == 200:
    #                     photo = await resp.read()
    #                     with NamedTemporaryFile(delete=False, mode='wb') as tmp_file:
    #                         tmp_file.write(photo)
    #                         tmp_file_path = tmp_file.name

    #                     media_files.append(types.InputMediaPhoto(
    #                         media=open(tmp_file_path, 'rb'),
    #                         caption=caption if idx == 0 else None,
    #                         parse_mode="HTML"
    #                     ))

    #                     os.remove(tmp_file_path)
    #                 else:
    #                     print(f"HTTP xatolik: {resp.status}")
    #                     return
    #         except Exception as e:
    #             print(f"Rasm yuklashda xatolik: {e}")
    #             return

    if media_files:
        await message.answer_media_group(media=media_files)
