import os

from pixabay import Image
from requests import get

PIXABAY_API = os.environ.get("PIXABAY_API")

if PIXABAY_API:
    PB_IMAGE = Image(PIXABAY_API)


def getPixabay(keyword):
    res = PB_IMAGE.search(keyword)
    if len(res["hits"]) > 0:
        return res["hits"][0]["largeImageURL"]
    else:
        return None


@borg.on(admin_cmd(pattern=r"pic (.*)"))
async def get_pic(event):
    key = event.text.removeprefix("pic ")
    if not PIXABAY_API:
        await event.edit("Please set PIXABAY_API")
        return
    await event.edit("Fetching your picture.....")
    url = getPixabay(key)
    if url is None:
        await event.edit("No pic found.")
        return
    image = get(url).content
    await event.client.send_file(event.chat_id, file=image)
    await event.delete()
