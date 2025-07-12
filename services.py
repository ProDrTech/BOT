import requests
from utils.env import BASE_URL
import aiohttp

def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    
    if response.status_code == 201:  
        data = response.json()
        return data
    else:
        print(response.status_code)


def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)  
    
    if response.status_code == 200: 
        data = response.json()
        return data
    else:
        print(response.status_code)


def putName(user_id, name):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.put(url, data={'name': name})
    print(response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        
        
        
def putPhone(user_id, phone):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.put(url, data={'phone': phone})
    print(response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
    
    

def getAbout():
    url = f"{BASE_URL}/about/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        

def getOrder(user_id):
    url = f"{BASE_URL}/order/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        print(response.status_code)    

def get_payment_links(user_id):
    payme_res = requests.post(f"{BASE_URL}/payment/create/", json={"user_id": user_id})
    click_res = requests.post(f"{BASE_URL}/payment/click/create/", json={"user_id": user_id})

    if payme_res.status_code == 200 and click_res.status_code == 200:
        return {
            "payme": payme_res.json().get("payment_link"),
            'click': click_res.json().get("payment_link"),
        }
    return None

def fetch_admin_link():
    response = requests.get(f"{BASE_URL}/admin/link/")
    if response.status_code == 200:
        return response.json().get("link")
    return "https://t.me/sizdaya"

GEMINI_API_KEY = "AIzaSyC5gUIikSRFuKehbccdrdSP86L5c-sjIKY"
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.0-flash:generateContent"
)

SYSTEM_PROMPT = """
Sen ASADMAXMUD brendi sun’iy intellekt yordamchisisan. 
Doimo o‘zbek tilida, foydali va samimiy tarzda javob ber.

ASADMAXMUD – bu O‘zbekistondagi keng qamrovli onlayn savdo platformasi. 
Mahsulotlar:
- Kiyim-kechak
- Uy-ro‘zg‘or buyumlari
- Oziq-ovqat mahsulotlari
- Gigiyena vositalari
- Bog‘dorchilik anjomlari
- Bolalar uchun o‘yinchoqlar va kiyimlar

ASADMAXMUD – faqat eng yaxshi mahsulotlarni taqdim etadi.
"""

def generate_prompt(user_message: str) -> str:
    return SYSTEM_PROMPT + "\nFoydalanuvchi savoli: " + user_message

async def ask_gemini(user_message: str) -> str:
    prompt = generate_prompt(user_message)
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GEMINI_URL, headers=headers, json=payload) as resp:
            data = await resp.json()
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                print("Gemini javobi olishda xato:", e)
                return "Kechirasiz, sun’iy intellekt bilan bog‘lanishda muammo yuz berdi."