import yaml
import requests
from time import sleep
from datetime import datetime
import re
import locale

locale.setlocale(locale.LC_ALL, '')

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
        convertedText = dt.strftime(status)

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

