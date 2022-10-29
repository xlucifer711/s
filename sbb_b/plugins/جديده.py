
from telethon.sync import errors
from telethon import events, functions, types
from sbb_b import sbb_b

@sbb_b.ar_cmd(pattern="كروباتي$")
async def oeo(event):
    result = await sbb_b(functions.channels.GetGroupsForDiscussionRequest())
    alist = []
    for item in result.chats:
        username = '  | @' + item.username if hasattr(item, 'username') and item.username  else " "
        roz = str(item.id) + ' | ' + item.title + username
        print(roz)
        alist.append(roz)
    if alist:
        await sbb_b.send_message('me', '\n'.join(alist))


@sbb_b.ar_cmd(pattern="الحاظرهم$")
async def main(event):
    result = await sbb_b(functions.contacts.GetBlockedRequest(
        offset=0,
        limit=1000000
    ))
    alist = []
    for user in result.users:
        if not user.bot:
            username = '@' + user.username if user.username else " "
            roz = f'{user.id} {user.first_name} {username}'
            print(roz)
            alist.append(roz)
    if alist:
        await sbb_b.send_message('me', '\n'.join(alist))

@sbb_b.ar_cmd(pattern="قيد (.*)")
async def se(event):
    exe = event.text[5:]
    try:
        result = await sbb_b(functions.messages.ToggleNoForwardsRequest(
            peer=exe,
            enabled=True
        ))
        await event.edit("تم بنجاح تفعيل وضع تقييد المحتوى")
    except errors.ChatNotModifiedError as e:
        print(e) #خاف ما تغير شي يعني القناة اصلا مفعل بيهل تقييد محتوى

@sbb_b.ar_cmd(pattern="نوعه (.*)")
async def se(event):
    exe = event.text[5:]
    x = await sbb_b.get_entity(exe)
    if hasattr(x, 'megagroup') and x.megagroup:
        await event.edit('نوع المعرف : كروب')
    elif hasattr(x, 'megagroup') and not x.megagroup:
        await event.edit('نوع المعرف : قناة')
    elif hasattr(x, 'bot') and x.bot:
        await event.edit('نوع المعرف : بوت')
    else:
        await event.edit('نوع المعرف : لحساب')



@sbb_b.ar_cmd(pattern="احذف (.*)")
async def se(event):
    exe = event.text[5:]
    await sbb_b.get_dialogs()
    chat = exe
    await sbb_b.delete_dialog(chat, revoke=True)    
    await event.edit("- تم بنجاح حذف الدردشة مع المستخدم بنجاح")

    
    
@sbb_b.ar_cmd(
    pattern="الزغرفة$",
    command=("الزغرفة", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "˛  َِ𝙘َِ𝘳ِ𝘪َِ𝘴َِ𝙏َِ𝘦َِ𝙉 ، ٰFٓoٍَِNٌtSَ\n"
                "•━═━═━═━═━━═━═━═━═━•\n"
                "**قائـمة اوامر الزغرفة :**\n"
                " `.زغرفة0`\n"
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
    
