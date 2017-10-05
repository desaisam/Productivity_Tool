import time

from datetime import datetime as dt

#We don't have to use datetime.datetime everytime


hosts_temp = 'hosts'
#Using /r allows us escape character
host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect  = '127.0.0.1'

sites_that_kill_me = ['www.facebook.com' ,'facebook.com', 'www.gmail.com' , 'www.flipkart.com' , 'www.ndtv.com']

print(dt.now())

while True:
    if dt(dt.now().year , dt.now().month, dt.now().day , 9) < dt.now() < dt(dt.now().year , dt.now().month, dt.now().day , 17) :
        print('Working hours: ')

        with open(host_path ,'r+') as file:
            content  = file.read() #this will load the entire file
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')

    else:
        with open(host_path , 'r+') as file:
            content = file.readlines()

            file.seek(0)

            for line in content :
                if not any(site in line for site in sites_that_kill_me):
                    file.write(line)

            file.truncate()
        print("EOD ! EOD ! EOD ! EOD !")

    time.sleep(5)
