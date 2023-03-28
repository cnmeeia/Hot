import datetime
import requests
import os

response = requests.get("https://api-new2020.vercel.app/36kr")

data = response.json()

now = datetime.datetime.now()

date_string = now.strftime("%m.%d_%H:%M")

dir_path = "/root/Hot/36kr"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
file_path = os.path.join(dir_path, f"{date_string}.md")

with open(file_path, "w", encoding="utf-8") as f:

    for item in data["data"]:
        title = item["title"]
        url = item["url"]

        f.write(f"[{title}]({url})\n\n")