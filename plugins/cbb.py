from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>📌 Language : Python3</b> 🐍\n<b>📌 Version : v1 </b>\n<b>📌 Developer : @HF_OWNER 😼</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 {query.from_user.username}\n\n🎖️ Available Plans :\n\n● {PRICE1} For Desi MMS Membership\n\n● {PRICE2} For Spy Membership ( B@th + Pi$$ + Hidden Cam )\n\n● {PRICE3} For Sn@p Le@ks Membership\n\n● {PRICE4} For Models Membership ( Ind + Pak + International)\n\n● {PRICE5} For Mega Links Membership\n\n\n💵 UPI ID -  <code>{UPI_ID}</code>\n\n\n📸 QR - ({UPI_IMAGE_URL})\n\n 📌You Will Get Lifetime Access + We Upload New Collection On Weekends‼️ \n\n ‼️ Must Send Screenshot After Payment",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("Send Payment Screenshot(ADMIN) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
            )
