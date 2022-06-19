import math

import pynewtonmath as newton
from AbishnoiRobot import dispatcher
from AbishnoiRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async


@run_async
def simplify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.simplify("{}".format(args[0])))


@run_async
def factor(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.factor("{}".format(args[0])))


@run_async
def derive(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.derive("{}".format(args[0])))


@run_async
def integrate(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.integrate("{}".format(args[0])))


@run_async
def zeroes(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.zeroes("{}".format(args[0])))


@run_async
def tangent(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.tangent("{}".format(args[0])))


@run_async
def area(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.area("{}".format(args[0])))


@run_async
def cos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))


@run_async
def sin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))


@run_async
def tan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))


@run_async
def arccos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))


@run_async
def arcsin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))


@run_async
def arctan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))


@run_async
def abs(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))


@run_async
def log(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))


__help__ = """
*MATHS*
Sᴏʟᴠᴇs ᴄᴏᴍᴘʟᴇx ᴍᴀᴛʜ ᴘʀᴏʙʟᴇᴍs ᴜsɪɴɢ ʜᴛᴛᴘs://ɴᴇᴡᴛᴏɴ.ɴᴏᴡ.sʜ
❍ /math *:* Mᴀᴛʜ `/ᴍᴀᴛʜ 2^2+2(2)`
❍ /factor *:* Fᴀᴄᴛᴏʀ `/ғᴀᴄᴛᴏʀ x^2 + 2x`
❍ /derive *:* Dᴇʀɪᴠᴇ `/ᴅᴇʀɪᴠᴇ x^2+2x`
❍ /integrate *:* Iɴᴛᴇɢʀᴀᴛᴇ `/ɪɴᴛᴇɢʀᴀᴛᴇ x^2+2x`
❍ /zeroes *:* Fɪɴᴅ 0's `/ᴢᴇʀᴏᴇs x^2+2x`
❍ /tangent *:* Fɪɴᴅ Tᴀɴɢᴇɴᴛ `/ᴛᴀɴɢᴇɴᴛ 2ʟx^3`
❍ /area *:* Aʀᴇᴀ Uɴᴅᴇʀ Cᴜʀᴠᴇ `/ᴀʀᴇᴀ 2:4ʟx^3`
❍ /cos *:* Cᴏsɪɴᴇ `/ᴄᴏs ᴘɪ`
❍ /sin *:* Sɪɴᴇ `/sɪɴ 0`
❍ /tan *:* Tᴀɴɢᴇɴᴛ `/ᴛᴀɴ 0`
❍ /arccos *:* Iɴᴠᴇʀsᴇ Cᴏsɪɴᴇ `/ᴀʀᴄᴄᴏs 1`
❍ /arcsin *:* Iɴᴠᴇʀsᴇ Sɪɴᴇ `/ᴀʀᴄsɪɴ 0`
❍ /arctan *:* Iɴᴠᴇʀsᴇ Tᴀɴɢᴇɴᴛ `/ᴀʀᴄᴛᴀɴ 0`
❍ /abs *:* Aʙsᴏʟᴜᴛᴇ Vᴀʟᴜᴇ `/ᴀʙs -1`
❍ /log *:* Lᴏɢᴀʀɪᴛʜᴍ `/ʟᴏɢ 2ʟ8`

_Kᴇᴇᴘ ɪɴ ᴍɪɴᴅ_: Tᴏ ғɪɴᴅ ᴛʜᴇ ᴛᴀɴɢᴇɴᴛ ʟɪɴᴇ ᴏғ ᴀ ғᴜɴᴄᴛɪᴏɴ ᴀᴛ ᴀ ᴄᴇʀᴛᴀɪɴ x ᴠᴀʟᴜᴇ, sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀs ᴄ|ғ(x) ᴡʜᴇʀᴇ ᴄ ɪs ᴛʜᴇ ɢɪᴠᴇɴ x ᴠᴀʟᴜᴇ ᴀɴᴅ ғ(x) ɪs ᴛʜᴇ ғᴜɴᴄᴛɪᴏɴ ᴇxᴘʀᴇssɪᴏɴ, ᴛʜᴇ sᴇᴘᴀʀᴀᴛᴏʀ ɪs ᴀ ᴠᴇʀᴛɪᴄᴀʟ ʙᴀʀ '|'. Sᴇᴇ ᴛʜᴇ ᴛᴀʙʟᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀɴ ᴇxᴀᴍᴘʟᴇ ʀᴇǫᴜᴇsᴛ.
Tᴏ ғɪɴᴅ ᴛʜᴇ ᴀʀᴇᴀ ᴜɴᴅᴇʀ ᴀ ғᴜɴᴄᴛɪᴏɴ, sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀs ᴄ:ᴅ|ғ(x) ᴡʜᴇʀᴇ ᴄ ɪs ᴛʜᴇ sᴛᴀʀᴛɪɴɢ x ᴠᴀʟᴜᴇ, ᴅ ɪs ᴛʜᴇ ᴇɴᴅɪɴɢ x ᴠᴀʟᴜᴇ, ᴀɴᴅ ғ(x) ɪs ᴛʜᴇ ғᴜɴᴄᴛɪᴏɴ ᴜɴᴅᴇʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ᴄᴜʀᴠᴇ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇ ᴛᴡᴏ x ᴠᴀʟᴜᴇs.
Tᴏ ᴄᴏᴍᴘᴜᴛᴇ ғʀᴀᴄᴛɪᴏɴs, ᴇɴᴛᴇʀ ᴇxᴘʀᴇssɪᴏɴs ᴀs ɴᴜᴍᴇʀᴀᴛᴏʀ(ᴏᴠᴇʀ)ᴅᴇɴᴏᴍɪɴᴀᴛᴏʀ. Fᴏʀ ᴇxᴀᴍᴘʟᴇ, ᴛᴏ ᴘʀᴏᴄᴇss 2/4 ʏᴏᴜ ᴍᴜsᴛ sᴇɴᴅ ɪɴ ʏᴏᴜʀ ᴇxᴘʀᴇssɪᴏɴ ᴀs 2(ᴏᴠᴇʀ)4. Tʜᴇ ʀᴇsᴜʟᴛ ᴇxᴘʀᴇssɪᴏɴ ᴡɪʟʟ ʙᴇ ɪɴ sᴛᴀɴᴅᴀʀᴅ ᴍᴀᴛʜ ɴᴏᴛᴀᴛɪᴏɴ (1/2, 3/4).
"""

__mod_name__ = "Mᴀᴛʜs"

SIMPLIFY_HANDLER = DisableAbleCommandHandler("math", simplify)
FACTOR_HANDLER = DisableAbleCommandHandler("factor", factor)
DERIVE_HANDLER = DisableAbleCommandHandler("derive", derive)
INTEGRATE_HANDLER = DisableAbleCommandHandler("integrate", integrate)
ZEROES_HANDLER = DisableAbleCommandHandler("zeroes", zeroes)
TANGENT_HANDLER = DisableAbleCommandHandler("tangent", tangent)
AREA_HANDLER = DisableAbleCommandHandler("area", area)
COS_HANDLER = DisableAbleCommandHandler("cos", cos)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs)
LOG_HANDLER = DisableAbleCommandHandler("log", log)

dispatcher.add_handler(SIMPLIFY_HANDLER)
dispatcher.add_handler(FACTOR_HANDLER)
dispatcher.add_handler(DERIVE_HANDLER)
dispatcher.add_handler(INTEGRATE_HANDLER)
dispatcher.add_handler(ZEROES_HANDLER)
dispatcher.add_handler(TANGENT_HANDLER)
dispatcher.add_handler(AREA_HANDLER)
dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)
