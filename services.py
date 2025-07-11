import requests
from utils.env import BASE_URL

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