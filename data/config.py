from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qib olamiz
PROVIDER_TOKEN_PAYCOM = env.str("PROVIDER_TOKEN_PAYCOM")
PROVIDER_TOKEN_CLICK = env.str("PROVIDER_TOKEN_CLICK")
ADMIN = env('ADMIN')

def check_provider_tokens():
    print("=== PROVIDER TOKEN TEKSHIRUVI ===")
    
    click_token = PROVIDER_TOKEN_CLICK
    payme_token = PROVIDER_TOKEN_PAYCOM
    
    print(f"Click token mavjud: {'✅' if click_token else '❌'}")
    print(f"Payme token mavjud: {'✅' if payme_token else '❌'}")
    
    if click_token:
        if ':TEST:' in click_token:
            print("Click token: TEST MODE ⚠️")
        elif ':LIVE:' in click_token:
            print("Click token: LIVE MODE ✅")
        else:
            print("Click token: NOMA'LUM FORMAT ❌")
    
    if payme_token:
        if ':TEST:' in payme_token:
            print("Payme token: TEST MODE ⚠️")
        elif ':LIVE:' in payme_token:
            print("Payme token: LIVE MODE ✅")
        else:
            print("Payme token: NOMA'LUM FORMAT ❌")
    
    print("=====================================")