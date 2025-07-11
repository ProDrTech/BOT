from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import buttons, texts
from services import getOrder, get_payment_links, fetch_admin_link
from handlers.order.getimage import download_and_send_image

@dp.message_handler(lambda message: message.text.startswith(buttons.MYORDER))
async def order_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    orders = getOrder(user_id)

    if not orders or not isinstance(orders, list):
        await message.answer(texts.ORDER_NOT)
        return

    total_price = 0
    is_all_paid = True

    for order in orders:
        is_paid_raw = order.get("is_paid", False)
        is_paid = str(is_paid_raw).lower() == "true"

        if not is_paid:
            is_all_paid = False
            order_items = order.get("order_items", [])
            for item in order_items:
                item_total_price = int(float(item["quantity"]) * float(item["price"]))
                total_price += item_total_price

        order_items = order.get("order_items", [])
        for item in order_items:
            item_total_price = int(float(item["quantity"]) * float(item["price"]))
            product = item['product']['name']
            color = item['color']['name']
            size = item['size']['size_name']
            quantity = item['quantity']
            price = int(float(item['price']))
            main_image = item['product'].get('main_image')
            color_image = item['color'].get('image')

            image_urls = [img for img in [main_image, color_image] if img]

            order_item_text = texts.order(
                product=product,
                color=color,
                size=size,
                quantity=quantity,
                price=price,
                item_total_price=item_total_price,
                is_paid=is_paid
            )

            if image_urls:
                try:
                    await download_and_send_image(image_urls, order_item_text, message)
                except Exception as e:
                    print(f"Xatolik: {e}")
                    await message.answer(order_item_text)
            else:
                await message.answer(order_item_text)

    # ✅ Hammasi to‘langan bo‘lsa, tugma chiqaramiz (sikl tashqarisida)
    if is_all_paid:
        link = fetch_admin_link()
        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton("📩 Admin bilan boglanish", url=link)
        )
        await message.answer(
            "✅ Buyurtmalaringiz to‘langan.\nAgar buyurtma haqida qo‘shimcha ma'lumot olishni istasangiz, pastdagi tugmani bosing:",
            reply_markup=keyboard
        )

    # 🔻 Aks holda, to‘lov tugmasi
    elif not is_all_paid:
        links = get_payment_links(user_id)
        if links:
            keyboard = InlineKeyboardMarkup(row_width=2)
            keyboard.add(
                InlineKeyboardButton("💰 Payme orqali", url=links['payme']),
                InlineKeyboardButton("💰 Click orqali", url=links['click']),
            )
            await message.answer(
                f"<b>Umumiy narx:</b> {total_price:,} so'm\n💰 To‘lov tizimidan birini tanlang:",
                reply_markup=keyboard
            )
        else:
            await message.answer("To‘lov havolasini olishda xatolik yuz berdi.")
