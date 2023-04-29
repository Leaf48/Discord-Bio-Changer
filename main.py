import yaml
import requests
from time import sleep
from datetime import datetime
import locale
import emoji

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class Bio:
    def __init__(self) -> None:
        with open("./config.yaml", encoding='utf-8', errors='ignore') as f:
            data = yaml.safe_load(f)

        self.data = data
        self.token = self.data["token"]
        
        if self.data["mode"] == "Bio":
            self.endpoint = "https://discord.com/api/v10/users/@me"
        else:
            self.endpoint = "https://discord.com/api/v10/users/@me/settings"
            
    
    def change(self, status: str) -> dict:
        dt = datetime.now()
        if dt.hour >= 12:
            time_str = f"PM"
        else:
            time_str = f"AM"

        # month m
        convertedText = status.replace(f"%m", f"{dt.month}")
        print(convertedText)
        # date d
        convertedText = convertedText.replace(f"%d", f"{dt.day}")
        print(convertedText)
        # am/pm p
        convertedText = convertedText.replace(f"%p", f"{time_str}")
        print(convertedText)
        # hour H
        convertedText = convertedText.replace(f"%H", f"{dt.hour}")
        print(convertedText)
        # minute M
        convertedText = convertedText.replace(f"%M", f"{dt.minute}")
        print(convertedText)
        # second S
        convertedText = convertedText.replace(f"%S", f"{dt.second}")
        print(convertedText)
        
        headers = {
            "cookie": "",
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        
        # Change Bio 
        if self.data["mode"] == "Bio":
            payload = {"bio": convertedText}

        # Change Status
        else:
            # t = convertedText
            # matches = re.findall(":.*?:", convertedText)
            # for i in matches:
            #     t = convertedText.replace(i, "")
            payload = {"custom_status": {"text": convertedText}}
        
        print(convertedText)

        res = requests.request("PATCH", self.endpoint, json=payload, headers=headers)

        return res.text
    
    def changeInstance(self):
        length = len(c.data["message"]) - 1

        i = 0
        while True:
            status = c.data["message"][i]
            change = self.change(status)
            # print(status, change)

            sleep(c.data["interval"])
            
            if i == length:
                i = 0
            else:
                i += 1
            
if __name__ == "__main__":
    c = Bio()
    # print(c.data)
    c.changeInstance()

