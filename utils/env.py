from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
GROUP_ID = list(map(int, env.list("GROUP_ID")))
WEBAPP_URL = env.str("WEBAPP_URL")
BASE_URL = env.str("BASE_URL")

# Adminlar ro'yxati: "7318128389,8148586285" => [7318128389, 8148586285]
ADMIN = list(map(int, env.list("ADMIN")))
