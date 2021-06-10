import time
import urllib.request
from datetime import datetime
import json


while True:
    with open("settings.json",'r') as f:
        jsondata=f.read()
        obj = json.loads(str(jsondata))
        urlobj=obj['urls']
        f.close()
    with open('log.txt','a') as f:
        for url in urlobj:
            y = datetime.now().strftime("%H %M")
            try:
                status_code = urllib.request.urlopen(url).getcode()
                website_is_up = status_code == 200.
                if website_is_up == False:
                    f.write(url+'  '+str(y)+'\n')
            except:
                f.write(url+'  '+str(y)+'\n')
    
    time.sleep(int(obj['interval']))