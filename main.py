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
        
        nowWeekFull = dt.weekday()
        if nowWeekFull == 0:
            nowWeekFull = "Monday"
        elif nowWeekFull == 1:
            nowWeekFull = "Tuesday"
        elif nowWeekFull == 2:
            nowWeekFull = "Wednesday"
        elif nowWeekFull == 3:
            nowWeekFull = "Thursday"
        elif nowWeekFull == 4:
            nowWeekFull = "Friday"
        elif nowWeekFull == 5:
            nowWeekFull = "Saturday"
        elif nowWeekFull == 6:
            nowWeekFull = "Sunday"
            
        nowWeekShort = dt.weekday()
        if nowWeekShort == 0:
            nowWeekShort = "Mon"
        elif nowWeekShort == 1:
            nowWeekShort = "Tue"
        elif nowWeekShort == 2:
            nowWeekShort = "Wed"
        elif nowWeekShort == 3:
            nowWeekShort = "Thu"
        elif nowWeekShort == 4:
            nowWeekShort = "Fri"
        elif nowWeekShort == 5:
            nowWeekShort = "Sat"
        elif nowWeekShort == 6:
            nowWeekShort = "Sun"

        # month m
        convertedText = status.replace(f"%m", f"{dt.month}")
        # date d
        convertedText = convertedText.replace(f"%d", f"{dt.day}")
        # week full W
        convertedText = convertedText.replace(f"%W", f"{nowWeekFull}")
        # week short w
        convertedText = convertedText.replace(f"%w", f"{nowWeekShort}")
        # am/pm p
        convertedText = convertedText.replace(f"%p", f"{time_str}")
        # hour H
        convertedText = convertedText.replace(f"%H", f"{dt.hour}")
        # minute M
        convertedText = convertedText.replace(f"%M", f"{dt.minute}")
        # second S
        convertedText = convertedText.replace(f"%S", f"{dt.second}")

        
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

