# edit by: @QQ070

import asyncio

from telethon import events, functions

from . import (
    ALIVE_NAME,
    PM_START,
    PMMENU,
    PMMESSAGE_CACHE,
    check,
    get_user_from_event,
    parse_pre,
    set_key,
)
from .sql_helper import pmpermit_sql as pmpermit_sql
from .sql_helper.globals import addgvar, delgvar, gvarstatus

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
CACHE = {}
PMPERMIT_PIC = Config.PMPERMIT_PIC or None
ICSS_PIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/57d51af1ca93d8cc8a958.jpg"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Rallsbot"
USER_BOT_WARN_ZERO = "⪼ لقد حذرتك من تكرار الرسائل . الآن تم حظرك والإبلاغ عنك حتى إشعار آخر.\n**- #ججـاو 🚶🏼‍♂️❕،** "


if Config.PRIVATE_GROUP_ID is not None:


    @bot.on(admin_cmd(pattern="الحمايه (تفعيل|تعطيل)$"))
    async def pmpermit_on(event):
        "Turn on/off pmpermit."
        input_str = event.pattern_match.group(1)
        if input_str == "تفعيل":
            if gvarstatus("pmpermit") is None:
                addgvar("pmpermit", "true")
                await edit_delete(
                    event, "**⌔∮تـم تفعيل أمـر حمايـة الخـاص بنجـاح 🔕☑️...**"
                )
            else:
                await edit_delete(event, "** ⌔∮ أمـر حمايـه الخـاص بالفعـل مُمكن  🔐✅**")
        elif gvarstatus("pmpermit") is not None:
            delgvar("pmpermit")
            await edit_delete(
                event, "**⌔∮تـم تعطيـل أمـر حمايـة الخـاص بنجاح 🔔☑️...**"
            )
        else:
            await edit_delete(event, "** ⌔∮ أمـر حمايـه الخـاص بالفعـل مُعطل 🔓✅**")


    @bot.on(admin_cmd(pattern="الحمايه (تفعيل|تعطيل)$"))
    async def pmpermit_on(event):
        "Turn on/off pmmenu."
        input_str = event.pattern_match.group(1)
        if input_str == "تعطيل":
            if gvarstatus("pmmenu") is None:
                addgvar("pmmenu", "false")
                await edit_delete(
                    event,
                    "**⌔∮تـم تعطيـل أمـر حمايـة الخـاص بنجاح 🔔☑️...**",
                )
            else:
                await edit_delete(
                    event, "** ⌔∮ أمـر حمايـه الخـاص بالفعـل مُعطل 🔓✅**"
                )
        elif gvarstatus("pmmenu") is not None:
            delgvar("pmmenu")
            await edit_delete(
                event, "**⌔∮تـم تفعيل أمـر حمايـة الخـاص بنجـاح 🔕☑️...**"
            )
        else:
            await edit_delete(
                event, "** ⌔∮ أمـر حمايـه الخـاص بالفعـل مُمكن  🔐✅**"
            )

     
    @bot.on(admin_cmd(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.text.startswith((".block", ".disapprove", ".سماح", ".رفض", ".approve")):
            return
        if (
            event.is_private
            and not pmpermit_sql.is_approved(chat.id)
            and chat.id not in PM_WARNS
        ):
            pmpermit_sql.approve(chat.id, "مرفوض")

    @bot.on(admin_cmd(pattern="سماح ?(.*)"))
    @bot.on(admin_cmd(pattern="a ?(.*)"))
    async def approve_p_m(event):
        if gvarstatus("pmpermit") is None:
            return await edit_delete(
                event,
                f"** ⌔∮ يـجب تفعيـل امـر الحـمايـه اولاً بإرسـال `.الحمايه تفعيل` لـيشتغل هذا الأمـر ...**",
            )
        if event.is_private:
            user = await event.get_chat()
            reason = event.pattern_match.group(1)
        else:
            user, reason = await get_user_from_event(event, secondgroup=True)
            if not user:
                return
            if not reason:
                reason = "Not mentioned"
        if not pmpermit_sql.is_approved(user.id):
            if user.id in PM_WARNS:
                del PM_WARNS[user.id]
            if user.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[user.id].delete()
                del PREV_REPLY_MESSAGE[user.id]
            if user.id in PM_START:
                PM_START.remove(user.id)
            pmpermit_sql.approve(user.id, reason)
            await edit_delete(
                event,
                f"**⪼ تمت الموافقه على** [{user.first_name}](tg://user?id={user.id}) 𓆰.",
                5,
            )
            if user.id in PMMESSAGE_CACHE:
                try:
                    await event.client.delete_messages(
                        user.id, PMMESSAGE_CACHE[user.id]
                    )
                except Exception as e:
                    LOGS.info(str(e))
        else:
            await edit_delete(
                event,
                f"[{user.first_name}](tg://user?id={user.id}) **موجود بـالفعل في قائمه السماح**",
                5,
            )

    @bot.on(admin_cmd(pattern="رفض ?(.*)"))
    @bot.on(admin_cmd(pattern="رفض ?(.*)"))
    async def disapprove_p_m(event):
        if gvarstatus("pmpermit") is None:
            return await edit_delete(
                event,
                f"** ⌔∮ يـجب تفعيـل امـر الحـمايـه اولاً بإرسـال `.الحمايه تفعيل` لـيشتغل هذا الأمـر ...**",
            )
        if event.is_private:
            user = await event.get_chat()
        else:
            input_str = event.pattern_match.group(2)
            if input_str == "الكل":
                return
            user, reason = await get_user_from_event(event, secondgroup=True)
            if reason == "all":
                return
            if not user:
                return
        if user.id in PM_START:
            PM_START.remove(user.id)
        if pmpermit_sql.is_approved(user.id):
            pmpermit_sql.disapprove(user.id)
            await edit_or_reply(
                event,
                f"**⪼ تم رفض** [{user.first_name}](tg://user?id={user.id}) 𓆰",
            )
        else:
            await edit_or_reply(
                event,
                f"[{user.first_name}](tg://user?id={user.id}) **لم تتم الموافقه عليه بعد**",
                5,
            )

    @bot.on(admin_cmd(pattern="بلوك(?: |$)(.*)"))
    async def block_p_m(event):
        if gvarstatus("pmpermit") is None:
            return await edit_delete(
                event,
                f"** ⌔∮ يـجب تفعيـل امـر الحـمايـه اولاً بإرسـال `.الحمايه تفعيل` لـيشتغل هذا الأمـر ...**",
            )
        if event.is_private:
            user = await event.get_chat()
        else:
            user, reason = await get_user_from_event(event)
            if not user:
                return
        if user.id in PM_START:
            PM_START.remove(user.id)
        await event.edit(
            f"** ⪼ أنت محظور الآن. لا يمكنك مراسلتي من الآن ..** [{user.first_name}](tg://user?id={user.id}) 𓆰"
        )
        await event.client(functions.contacts.BlockRequest(user.id))

    @bot.on(admin_cmd(pattern="انبلوك(?: |$)(.*)"))
    async def unblock_pm(event):
        if gvarstatus("pmpermit") is None:
            return await edit_delete(
                event,
                f"** ⌔∮ يـجب تفعيـل امـر الحـمايـه اولاً بإرسـال `.الحمايه تفعيل` لـيشتغل هذا الأمـر ...**",
            )
        if event.is_private:
            user = await event.get_chat()
        else:
            user, reason = await get_user_from_event(event)
            if not user:
                return
        await event.client(functions.contacts.UnblockRequest(user.id))
        await event.edit(
            f"** ⪼ أنت غير محظور الآن. يمكنك مراسلتي من الآن ..** [{user.first_name}](tg://user?id={user.id})"
        )

    @bot.on(admin_cmd(pattern="المسموح لهم$"))
    async def approve_p_m(event):
        if gvarstatus("pmpermit") is None:
            return await edit_delete(
                event,
                f"** ⌔∮ يـجب تفعيـل امـر الحـمايـه اولاً بإرسـال `.الحمايه تفعيل` لـيشتغل هذا الأمـر ...**",
            )
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "𓆰 𝙎𝙊𝙐𝙍𝘾𝙀 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 - 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        if len(approved_users) > 0:
            for sender in approved_users:
                if sender.reason:
                    APPROVED_PMs += f"⪼ [{sender.chat_id}](tg://user?id={sender.chat_id}) **for ↫** {sender.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"⪼ [{sender.chat_id}](tg://user?id={sender.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "**⪼ انت لم توافق على اي شخص حتى الان 𓆰.**"
        await edit_or_reply(
            event,
            APPROVED_PMs,
            file_name="approvedpms.txt",
            caption="**قائمه السماح**",
        )

    @bot.on(admin_cmd(pattern="رفض الكل$"))
    @bot.on(admin_cmd(pattern="رفض الكل$"))
    async def disapprove_p_m(event):
        if gvarstatus("pmpermit") is None:
            return await edit_delete(
                event,
                f"** ⌔∮ يـجب تفعيـل امـر الحـمايـه اولاً بإرسـال `.الحمايه تفعيل` لـيشتغل هذا الأمـر ...**",
            )
        if event.fwd_from:
            return
        result = "**⪼ حسنـاً ، الجميـع مرفـوض الان... 🚸𓆰**"
        pmpermit_sql.disapprove_all()
        await edit_delete(event, result, parse_mode=parse_pre, time=10)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if gvarstatus("pmpermit") is None:
            return
        if event.sender_id == event.client.uid:
            return
        if Config.PRIVATE_GROUP_ID is None:
            return
        if not event.is_private:
            return
        chat_id = event.sender_id
        if chat_id in CACHE:
            sender = CACHE[chat_id]
        else:
            sender = await event.get_chat()
            CACHE[chat_id] = sender
        if sender.bot or sender.verified:
            return
        if PMMENU:
            if event.raw_text == "/start":
                if chat_id not in PM_START:
                    PM_START.append(chat_id)
                set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
                return
            if len(event.raw_text) == 1 and check(event.raw_text):
                set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
                return
            if chat_id in PM_START:
                return
        if not pmpermit_sql.is_approved(chat_id):
            await do_pm_permit_action(chat_id, event, sender)

    async def do_pm_permit_action(chat_id, event, sender):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_PMS:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(1)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            if chat_id in PM_START:
                PM_START.remove(chat_id)
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = f"**#تم_حظره من الخاص**\
                            \n ⪼ [المستخدم](tg://user?id={chat_id}) : {chat_id}\
                            \n ⪼ عدد الرسائل : {PM_WARNS[chat_id]}"
            try:
                await event.client.send_message(
                    entity=Config.PRIVATE_GROUP_ID,
                    message=the_message,
                )
                return
            except BaseException:
                return
        me = await event.client.get_me()
        mention = f"[{sender.first_name}](tg://user?id={sender.id})"
        my_mention = f"[{me.first_name}](tg://user?id={me.id})"
        first = sender.first_name
        last = sender.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{sender.username}" if sender.username else mention
        userid = sender.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        totalwarns = Config.MAX_FLOOD_IN_PMS + 1
        warns = PM_WARNS[chat_id] + 1
        if PMMENU:
            if Config.CUSTOM_PMPERMIT_TEXT:
                USER_BOT_NO_WARN = Config.CUSTOM_PMPERMIT_TEXT.format(
                    mention=mention,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                    my_first=my_first,
                    my_last=my_last,
                    my_fullname=my_fullname,
                    my_username=my_username,
                    my_mention=my_mention,
                    totalwarns=totalwarns,
                    warns=warns,
                )
            else:

                USER_BOT_NO_WARN = (
                    f"𓆩𝙎𝙊𝙐𝙍𝘾𝙀 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 - 𝑷𝑴 𝑺𝑬𝑪𝑼𝑹𝑰𝑻𝒀𓆪\n◐━─━─━─━─𝐑𝐀𝐈𝐈𝐒─━─━─━─━◐\n\n❞ **هها هلو**  {mention} ❝\n\n **⤶ انا مشغـول حـالياً لا تقـم بازعـاجي وارسـال رسـائل كثيـره والا سـوف يتم حظـرك تلقـائياً.....**"
                    f"**فقط قل سبب مجيئك وانتظـر حتى اعـود لكـي تتـم الموافقـه عليك**.\
                                    \n\n ⤶ ❨ **عندك** {warns}/{totalwarns} **تحذيرات** ❩"
                )
        else:
            if Config.CUSTOM_PMPERMIT_TEXT:
                USER_BOT_NO_WARN = Config.CUSTOM_PMPERMIT_TEXT.format(
                    mention=mention,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                    my_first=my_first,
                    my_last=my_last,
                    my_fullname=my_fullname,
                    my_username=my_username,
                    my_mention=my_mention,
                    totalwarns=totalwarns,
                    warns=warns,
                )
            else:
                USER_BOT_NO_WARN = (
                    f"𓆩𝙎𝙊𝙐𝙍𝘾𝙀 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 - 𝑷𝑴 𝑺𝑬𝑪𝑼𝑹𝑰𝑻𝒀𓆪\n◐━─━─━─━─𝐑𝐀𝐈𝐈𝐒─━─━─━─━◐\n\n❞ **هها هلو**  {mention} ❝\n\n **⤶ انا مشغـول حـالياً لا تقـم بازعـاجي وارسـال رسـائل كثيـره والا سـوف يتم حظـرك تلقـائياً.....**"
                    f"**فقط قل سبب مجيئك وانتظـر حتى اعـود لكـي تتـم الموافقـه عليك**.\
                                    \n\n ⤶ ❨ **عندك** {warns}/{totalwarns} **تحذيرات** ❩"
                )
        if PMPERMIT_PIC:
            r = await event.reply(USER_BOT_NO_WARN, file=PMPERMIT_PIC)
        else:
            r = await event.reply(USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        return None


@bot.on(events.NewMessage(incoming=True, from_users=(2019189055)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**مطوري الغـالي هنا يتمشى 🥳♥️𓆰**")
            await borg.send_message(chat, "**⪼ اطـلق هـلاو مطـوري الغـالي الريس علش اننـي محظـوظ لقدومـك الـي 🙈♥️𓆰**")

#علا-أص-تمس-ملا-مجهول-رام-علش-ابرا-اسا-انا
@bot.on(events.NewMessage(incoming=True, from_users=(2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055, 2019189055)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**مطوري الغـالي هنا يتمشى 🥳♥️𓆰**")
            await borg.send_message(chat, "**⪼ اطـلق هـلاو احد مطـورين السـورس هنا اننـي محظـوظ لقدومـك الـي 🙈♥️𓆰**")


CMD_HELP.update(
    {
        "الحمايه": "**اسم الاضافـه : **`الحمايه`\
        \n\n    **╮•❐ الامـر ⦂ **`.الحمايه تفعيل`\
        \n  •  **الشـرح •• **__لتفعيـل حمايـة الخـاص والـرد التلقائـي للاشخـاص الذين يراسلونك في الخاص__\
        \n\n    **╮•❐ الامـر ⦂ **`.الحمايه تعطيل`\
        \n  •  **الشـرح •• **__لتعطيل حمايـة الخـاص والـرد التلقائـي للاشخـاص الذين يراسلونك في الخاص__\
        \n\n    **╮•❐ الامـر ⦂ **`.سماح`\
        \n  •  **الشـرح •• **__للسمـاح للاشخـاص بالرد ع الشخـص__\
        \n\n    **╮•❐ الامـر ⦂ **`.رفض`\
        \n  •  **الشـرح •• **__لـرفض الاشخـاص بالرد ع الشخـص__\
        \n\n    **╮•❐ الامـر ⦂ **`.بلوك`\
        \n  •  **الشـرح •• **__لحـظر شخص__\
        \n\n    **╮•❐ الامـر ⦂ **`.انبلوك`\
        \n  •  **الشـرح •• **__الغـاء حظر شخص.__\
        \n\n    **╮•❐ الامـر ⦂ **`.المسموح لهم`\
        \n  •  **الشـرح •• **__لعـرض قائمـه بالاشخـاص المسمـوح لهـم.__\
        \n\n    **╮•❐ الامـر ⦂ **`.رفض الكل`\
        \n  •  **الشـرح •• **__لـرفض كل الاشخاص المسموح لهم.__\
        \n\n  •  Available variables for formatting `CUSTOM_PMPERMIT_TEXT` :\
        \n`{mention}`, `{first}`, `{last} `, `{fullname}`, `{userid}`, `{username}`, `{my_first}`, `{my_fullname}`, `{my_last}`, `{my_mention}`, `{my_username}`,`{warns}` , `{totalwarns}`.\
"
    }
)
