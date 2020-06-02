# Copyright (C) 2020 azrim.
# All rights reserved.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import pyshorteners
from re import match
from userbot import bot, CMD_HELP, BITLY_TOKEN, BOTLOG, BOTLOG_CHATID
from userbot.events import register


@register(outgoing=True, pattern=r"^.short(?: |$)(.*)")
async def shortener(short):
    """
        Shorten link using bit.ly API
    """
    if BITLY_TOKEN is not None:
        token = BITLY_TOKEN
        reply = await short.get_reply_message()
        message = short.pattern_match.group(1)
        if message:
            pass
        elif reply:
            message = reply.text
        else:
            await short.edit("`Error! No URL given!`")
            return
        link_match = match(r'\bhttps?://.*\.\S+', message)
        if link_match:
            pass
        else:
            await short.edit("`Error! Please provide valid url!`\nexample: https://google.com")
            return
        s = pyshorteners.Shortener(api_key='{token}')
        raw_output = s.bitly.short('{message}')
        string_output = f"{raw_output}"
        output = string_output.replace("'", "").replace("'", "")
        await short.edit(f"`Your link shortened successfully!`\nHere is your link {output}")
        if BOTLOG:
           await short.client.send_message(BOTLOG_CHATID, f"`#SHORTLINK \nThis Your Link!`\n {output}")
    else:
        await short.edit(f"Set bit.ly API token first\nGet from [here](https://bitly.com/a/sign_up)")


@register(outgoing=True, pattern=r"^.expand(?: |$)(.*)")
async def expander(expand):
    """
        Expand Shortened link using bit.ly API
    """
    if BITLY_TOKEN is not None:
        token2 = BITLY_TOKEN
        reply1 = await expand.get_reply_message()
        message1 = expand.pattern_match.group(1)
        if message1:
            pass
        elif reply1:
            message1 = reply1.text
        else:
            await expand.edit("`Error! No URL given!`")
            return
        link_match1 = match(r'\bhttps?://.*\.\S+', message1)
        if link_match1:
            pass
        else:
            await expand.edit("`Error! Please provide valid url!`\nexample: https://google.com")
            return
        s1 = pyshorteners.Shortener(api_key='token2')
        raw_output1 = s1.bitly.expand('{message1}')
        string_output1 = f"{raw_output1}"
        output1 = string_output1.replace("'", "").replace("'", "")
        await expand.edit(f"`Your link expanded successfully!`\nHere is your link {output1}")
        if BOTLOG:
           await expand.client.send_message(BOTLOG_CHATID, f"`#SHORTLINK \nThis Your Link!`\n {output1}")
    else:
        await expand.edit(f"Set bit.ly API token first\nGet from [here](https://bitly.com/a/sign_up)")


@register(outgoing=True, pattern=r"^.bitly(?: |$)(.*)")
async def clicked(click):
    """
        Expand Shortened link using bit.ly API
    """
    if BITLY_TOKEN is not None:
        token3 = BITLY_TOKEN
        reply2 = await click.get_reply_message()
        message2 = click.pattern_match.group(1)
        if message2:
            pass
        elif reply2:
            message2 = reply2.text
        else:
            await click.edit("`Error! No URL given!`")
            return
        link_match2 = match(r'\bhttps?://.*\.\S+', message2)
        if link_match2:
            pass
        else:
            await click.edit("`Error! Please provide valid url!`\nexample: https://google.com")
            return
        s2 = pyshorteners.Shortener(api_key='token3')
        raw_output2 = s2.bitly.clicks('{message2}')
        string_output2 = f"{raw_output2}"
        output2 = string_output2.replace("'", "").replace("'", "")
        await click.edit(f"Your [link]('{urls2}') has been clicked for `{output2} times`")
        if BOTLOG:
           await click.client.send_message(BOTLOG_CHATID, f"`#SHORTLINK \nYour link has been clicked for {output2} times")
    else:
        await click.edit(f"Set bit.ly API token first\nGet from [here](https://bitly.com/a/sign_up)")


CMD_HELP.update({
    "bitly":
    "`.short` <url> or reply to message contains url"
    "\nUsage: Shorten link using bit.ly API"
    "\n\n`.expand` <url> or reply to message contains url"
    "\nUsage: Shorten link using bit.ly API"
    "\n\n`.bitly` <url> or reply to message contains url"
    "\nUsage: Show your link statistics"
})
