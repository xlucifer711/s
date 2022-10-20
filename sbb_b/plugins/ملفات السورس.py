from sbb_b import sbb_b 

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _catutils, parse_pre, yaml_format

plugin_category = "tools"


@sbb_b.ar_cmd(
    pattern="الملفات$",
    command=("الملفات", plugin_category),
    info={
        "header": "To list all plugins in jepthon.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in sbb_b"
    cmd = "ls sbb_b/plugins"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = f"**[بوت كرستين](tg://need_update_for_some_feature/) الـمـلفـات:**\n{o}"
    await edit_or_reply(event, OUTPUT)


@sbb_b.ar_cmd(
    pattern="فاراتي$",
    command=("فاراتي", plugin_category),
    info={
        "header": "To list all environment values in sbb_b.",
        "description": "to show all heroku vars/Config values in your sbb_b",
        "usage": "{tr}env",
    },
)
async def _(event):
    "To show all config values in jepthon"
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (
        f"**[بوت كرستين](tg://need_update_for_some_feature/) قـائمـة الـفـارات:**\n\n\n{o}"
    )
    await edit_or_reply(event, OUTPUT)

@sbb_b.ar_cmd(
    pattern="متى$",
    command=("متى", plugin_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await edit_or_reply(
        event, f"**⌯︙نـشـرت هـذه الـرسالة فـي  :** `{yaml_format(result)}`"
    )
