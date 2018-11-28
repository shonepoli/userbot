from telethon import events
import os
import requests
import json

APP_ID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

@borg.on(events.NewMessage(pattern=r"\.weather (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(input_str, APP_ID)).json()
    if response_api["cod"] == 200:
        await event.edit("The temperature is around {}°C, in {}.".format(response_api["main"]["temp"], input_str))
    else:
        await event.edit(response_api["message"])
