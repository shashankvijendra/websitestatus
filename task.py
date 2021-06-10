import time
import urllib.request
import re
import timeit
from datetime import datetime
# def websitecheck():
while True:
    c= open("settings.json",'r')
    data=c.readlines()
    list_data = []
    var = 0
    for i in data:
        if "interval" in i:
            list_data.append(i.split(':')[1])
            var=0
            timedata = i.split(':')[1]
        elif "urls" in i:
            var+=1
            list_data.append(i.split('"urls"')[0])
        elif var == 1 : 
            list_data.append(i.split(']')[0])
        elif "]," in i:
            list_data.append(i.split(',')[0])
            # print(i.split(']')[0])
    # print(list_data)
    c.close()
    with open('log.txt','a') as f:
        f.write(time.ctime()+'\n')
        
        for j in list_data:
            # print(j.strip())
            
            if len(j) > 5:
                url =j.strip()
                # print(url.rstrip(','))
                url = url.replace(',','')
                # print(re.findall('"([^"]*)"', url))
                y = datetime.now().strftime("%H %S")
                
                try:
                    status_code = urllib.request.urlopen(re.findall('"([^"]*)"', url)[0]).getcode()
                    website_is_up = status_code == 200.
                    # print(website_is_up)
                    if website_is_up == False:
                        
                        f.write(url+'  '+str(y)+'\n')

                except:
                    y = datetime.now()
                    
                    f.write(url+'  '+str(y)+'\n')
        f.close()
    
    time.sleep(int(timedata))




