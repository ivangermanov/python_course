import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]

while True:
    now = dt.now()
    min_time = dt(now.year,now.month, now.day, 14)
    max_time = dt(now.year,now.month, now.day, 18)
    if now > min_time and now < max_time: #min_time < now < max_time
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n") 
    else:
        print("Relax hours...")
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)