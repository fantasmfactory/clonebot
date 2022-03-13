#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5108256911:AAEmr4BoWNGLsLogmpuh9-RqQQbY3ysLIYs")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "7664988"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "11e0d24d71cef15a43192e227c8efee9")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "710532288").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAjy1_h2Uh1-DPPOE_4IaYZ-zZ_aUSmyQDH4qxvBLCDzfHZNM1Fc847NZaWYGlc0HMknS6IjxSGGTixtQwTI6QCrhBT3yh8-4eDRVXzAfidYPAEaH3fCNJ5Dkd95hGE405wKHh4BGfSMZWrAnn9XUe1Kba2GE_UASP1iLgOBFlWYDDEJkyCVuy-cjHHVFGSpeJ_3Kdcah9oC4zw3w5VdFPVDNEC7tEHtGV-8uEIMX9WFQVFqVyzMqe96M9Ll5WwChSuq70MyKpo3LHRC9jdOVdHLYU_NrFg8ZsinGrgXmrfL8XOGx79pex0WvzPJuC2RuDTAoJ650yc6nViYlYMsiNGAAAAATNguUQB")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "https://clone-waifu-bot.herokuapp.com")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
