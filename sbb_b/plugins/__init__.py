import math
import os
import re
import time

import heroku3
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..core.session import sbb_b
from ..helpers import *
from ..helpers.utils import _format, _jmthonutils, install_pip, reply_id
from ..sql_helper.globals import gvarstatus

bot = sbb_b
LOGS = logging.getLogger(__name__)
USERID = sbb_b.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

mention = f"[{Config.ALIVE_NAME}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{Config.ALIVE_NAME}</a>"

PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD

# Gdrive
G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET
G_DRIVE_DATA = Config.G_DRIVE_DATA
G_DRIVE_FOLDER_ID = Config.G_DRIVE_FOLDER_ID
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

ban_rz = "razan/razan/حظر.jpg"
mute_rz = "razan/razan/كتم.jpg"
promote_rz = "razan/razan/رفع.jpg"
demote_rz = "razan/razan/تنزيل.jpg"


PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None


if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


if Config.THUMB_IMAGE is not None:
    if check := url(Config.THUMB_IMAGE):
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
