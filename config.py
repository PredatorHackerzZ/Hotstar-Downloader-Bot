import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = "1746903731:AAExBqFKz2SeNCe1Q6V7kd6qodYO2yepC0w"

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = 924859
    API_HASH = "a4c9a18cf4d8cb24062ff6916597f832"

    # Array to store users who are authorized to use the bot
    AUTH_USERS = "1002182448"

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Generate screenshots for file after uploading
    # Defaults to True
    SCREENSHOTS = True

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600

    # watermark file
    DEF_WATER_MARK_FILE = "Uploaded By: @Hx URLUpload Bot"

    # Sql Database url
    DB_URI = "postgres://jeohpdfhlhdgtz:591ee700f7c2d4b3f368e2c10599bf5b372bce649f51b47b2110c2813f479a60@ec2-52-45-73-150.compute-1.amazonaws.com:5432/d9470iujavjoqb"

