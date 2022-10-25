from sbb_b import *
from sbb_b import sbb_b 
from ..sql_helper.globals import gvarstatus

@sbb_b.on(admin_cmd(pattern="(ذاتية|ذاتيه)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    sbb_b = await event.get_reply_message()
    pic = await sbb_b.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم جـلب الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @cr_source 
- Dev: @wjj_u 
  """,
    )
    await event.edit(" 🙂❤️ ")
