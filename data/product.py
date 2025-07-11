from aiogram import types
from aiogram.types import LabeledPrice, ShippingOption
from utils.product import Product
from data.config import PROVIDER_TOKEN_PAYCOM

asadmaxmud_product = Product(
    title="Asadmaxmud Quritilgan Mevalari",
    description="Asadmaxmud mahsulotlari",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Quritilgan Mevalari",
            amount=10000000 # 100 000.00 so'm yuz ming so'm
        ),
        LabeledPrice(
            label="Yetkazib berish (7 kun)",
            amount=5000000  # 50 000.00 so'm ellik ming so'm
        )
    ],
    provider_token=PROVIDER_TOKEN_PAYCOM,
    start_parameter="create_invoice_asadmaxmud",
    photo_url="https://files.glotr.uz/company/000/023/705/products/2021/04/23/2021-04-23-17-06-02-003701-fb3640526a073012ff1470d35273cba8.jpeg?_=ozb9y",
    photo_height=851,
    photo_width=1280,
    # photo_size=500,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # yetkazib berish manzili
    is_flexible=True,
)

REGULAR_SHIPPING = ShippingOption(
    id="post_reg",
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            label="Maxsus quti",
            amount=1000000  # 10 000.00 so'm o'n ming so'm
        ),
        LabeledPrice(
            label="3 ish kuniga yetkazish",
            amount=1000000  # 10 000.00 so'm o'n ming so'm
        )
    ]
)

FAST_SHIPPING = ShippingOption(
    id="post_fast",
    title="Express pochta (1 kun)",
    prices=[
        LabeledPrice(
            label="1 kunda yetkazish",
            amount=1000000  # 10 000.00 so'm o'n ming so'm
        )
    ]
)

PICKUP_SHIPPING = ShippingOption(
    id="pickup",
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice(
            label="Yetkazib berishsiz",
            amount=-1000000  # 10 000.00 so'm o'n ming so'm
        )
    ]
)