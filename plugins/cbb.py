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
            text=f"👋 {query.from_user.username}\n\n🎖️ **Available Membership Plans:**\n\n🔹 **{PRICE1}** – 7 Days Prime Membership\n🔹 **{PRICE2}** – 1 Month Prime Membership\n🔹 **{PRICE3}** – 3 Months Prime Membership\n🔹 **{PRICE4}** – 6 Months Prime Membership\n🔹 **{PRICE5}** – 1 Year Prime Membership\n\n🔥 **Exclusive Categories:**\n🔸 **Desi MMS Membership** – {PRICE1}\n🔸 **Spy Membership** *(B@th + Pi$$ + Hidden Cam)* – {PRICE2}\n🔸 **Sn@p Le@ks Membership** – {PRICE3}\n🔸 **Models Membership** *(Ind + Pak + International)* – {PRICE4}\n🔸 **Mega Links Membership** – {PRICE5}\n\n💰 **Payment Details:**\n💵 **UPI ID:** <code>{UPI_ID}</code>\n📸 **QR Code:** [Click Here to Scan]({UPI_IMAGE_URL})\n♻️ **For Crypto Payments:** [@Crypto_Paymentss](https://t.me/Crypto_Paymentss)\n\n✅ **Perks of Membership:**\n✔️ Lifetime Access\n✔️ Fresh Content Uploaded Every Weekend\n\n‼️ *Must send a screenshot after payment for verification!*",
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
