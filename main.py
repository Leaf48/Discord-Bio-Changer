import yaml
import requests
from time import sleep
from datetime import datetime

class Bio:
    def __init__(self) -> None:
        with open("config.yaml") as f:
            data = yaml.safe_load(f)

        self.data = data
        self.token = self.data["token"]
        
        self.endpoint = "https://discord.com/api/v10/users/@me"
    
    def change(self, status: str) -> dict:
        dt = datetime.now()
        convertToDate = dt.strftime(status) 

        payload = {"bio": convertToDate}

        headers = {
            "cookie": "",
            "Content-Type": "application/json",
            "Authorization": self.token
        }

        res = requests.request("PATCH", self.endpoint, json=payload, headers=headers)

        return res.text
    
    def changeInstance(self):
        length = len(c.data["message"]) - 1

        i = 0
        while True:
            status = c.data["message"][i]
            change = self.change(status)
            print(status, change)
            
            sleep(c.data["interval"])
            
            if i == length:
                i = 0
            else:
                i += 1
            
if __name__ == "__main__":
    c = Bio()
    print(c.data)
    c.changeInstance()

