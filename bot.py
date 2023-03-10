import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "šš¼š š¦šš®šæšš²š± š£š¹š²š®šš² š¦ššÆšš°šæš¶šÆš² š¢š½ššš§š²š°šµš",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("ššæš³š°šš“š", url="https://t.me/MWUpdatez"),
      InlineKeyboardButton("šššæšæš¾šš", url="https://t.me/OpusTechz")
      ],[
      InlineKeyboardButton("ššš±šš²ššøš±š“", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
      ]]
    await message.reply_text(text="**š·š“š»š»š¾...ā”\n\nšøš°š¼ š° ššøš¼šæš»š“ šš“š»š“š¶šš°š¼ š°ššš¾ šš“ššš“šš š°š²š²š“šæš š±š¾š.\nšµš¾š šš¾šš š²š·š°šš š²šš“š°šš“ š¾š½š“ š±š¾š... \nššøš³š“š¾ š¾š½ š¼š šš¾šššš±š“ š²š·š°š½š½š“š»**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request()
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} š¹š¾šøš½š“š³ ā”") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("šš¼š š¦šš®šæšš²š± š£š¹š²š®šš² š¦ššÆšš°šæš¶šÆš² š¢š½ššš§š²š°šµš")
pr0fess0r_99.run()
