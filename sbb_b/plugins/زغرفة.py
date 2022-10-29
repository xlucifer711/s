import random

from sbb_b import sbb_b 

from ..core.managers import edit_or_reply
from . import fonts

plugin_category = "extra"


@sbb_b.ar_cmd(
    pattern="الزغرفة$",
    command=("الزغرفة", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "˛  َِ𝙘َِ𝘳ِ𝘪َِ𝘴َِ𝙏َِ𝘦َِ𝙉 ، ٰFٓoٍَِNٌtSَ\n"
                "•━═━═━═━═━━═━═━═━═━•\n"
                "**قائـمة اوامر الزغرفة :**\n"
                " `.زغرفة1`\n"
                " `.زغرفة2`\n"
                " `.زغرفة3`\n"
                " `.زغرفة4`\n"
                " `.زغرفة5`\n"
                " `.زغرفة6`\n"
                " `.زغرفة7`\n"
                " `.زغرفة8`\n"
                " `.زغرفة9`\n"
                " **اكتب الاسم مع الامر للـزغرفة فقط انكليزي**\n"
                "•━═━═━═━═━━═━═━═━═━•‌‌\n"
                "˛ ََِِ𝗰.ًًٍٍ𝗥 ًًٍٍ𝗨ٍّّ𝘀ََِِ𝗲ًًٍٍ𝗥ًًٍٍ𝗕ُُ𝗼ٖٔ𝗧- [CَِٓHُ](t.me/cr_source)"    
   

@sbb_b.ar_cmd(
    pattern="زغرفة1(?:\s|$)([\s\S]*)",
    command=("زغرفة1", plugin_category),)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            musicalcharacter = fonts.musicalfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, musicalcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة2(?:\s|$)([\s\S]*)",
    command=("زغرفة2", plugin_category),)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🌺😗🗿**")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            ancientcharacter = fonts.ancientfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, ancientcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة3(?:\s|$)([\s\S]*)",
    command=("زغرفة3", plugin_category),)
async def vapor(event):
    "Changes font style of the given text"
    reply_text = []
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(event, "اعـطنـي نـص اولا 🧸♥")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await edit_or_reply(event, "".join(reply_text))


@sbb_b.ar_cmd(
    pattern="زغرفة4(?:\s|$)([\s\S]*)",
    command=("زغرفة4", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة5(?:\s|$)([\s\S]*)",
    command=("زغرفة5", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة6(?:\s|$)([\s\S]*)",
    command=("زغرفة6", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة7(?:\s|$)([\s\S]*)",
    command=("زغرفة7", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            tantextcharacter = fonts.tantextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة8(?:\s|$)([\s\S]*)",
    command=("زغرفة8", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            littleboxtextcharacter = fonts.littleboxtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة9(?:\s|$)([\s\S]*)",
    command=("زغرفة9", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwcapitalcharacter = fonts.hwcapitalfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, hwcapitalcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة10(?:\s|$)([\s\S]*)",
    command=("زغرفة10", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            doubletextcharacter = fonts.doubletextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, doubletextcharacter)
    await edit_or_reply(event, string)


@sbb_b.ar_cmd(
    pattern="زغرفة0(?:\s|$)([\s\S]*)",
    command=("زغرفة0", plugin_category),
)
async def spongemocktext(mock):
    "Changes font style of the given text"
    reply_text = []
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(mock, "اعـطنـي نـص اولا")
        return

    for charac in message:
        if charac.isalpha() and random.randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await edit_or_reply(mock, "".join(reply_text))
