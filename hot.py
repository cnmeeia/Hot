import datetime
import requests

response = requests.get("https://api-new2020.vercel.app/bilibili")


data = response.json()

now = datetime.datetime.now()

date_string = now.strftime("%Y.%m.%d_%H:%M:%S")

with open(f"{date_string}.md", "w", encoding="utf-8") as f:

    for item in data["data"]:
        title = item["title"]
        url = item["url"]
        mobile_url = item["mobileUrl"]

        f.write(f"{title}  {url} {mobile_url}\n\n")
