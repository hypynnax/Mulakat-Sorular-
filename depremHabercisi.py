import requests
import datetime
from smtplib import SMTP
import time
from bs4 import BeautifulSoup

def veriCek():
    global depremler
    url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    depremler = soup.find("pre").get_text().strip()[584:].split("\n")

def karsilastir():
    global eskiDeprem, yer, siddet
    for deprem in depremler:
        guncelDeprem = datetime.datetime(int(deprem[0:4]), int(deprem[5:7]), int(deprem[8:10]), int(deprem[11:13]), int(deprem[14:16]), int(deprem[17:19]))
        gecenSure = guncelDeprem.timestamp() - eskiDeprem.timestamp()
        if gecenSure > 0:
            eskiDeprem = guncelDeprem
            yer = deprem[71:121].strip()
            siddet = deprem[59:65].strip()
            if float(siddet) > 4.0:
                haberVer()

def haberVer():
    mesaj = "Deprem Uyarısı\n{:02}.{:02}.{} {:02}:{:02}:{:02}'de {}'da {} şiddetinde deprem meydana geldi.".format(eskiDeprem.day, eskiDeprem.month, eskiDeprem.year, eskiDeprem.hour, eskiDeprem.minute, eskiDeprem.second, yer, siddet)
    try:
        mail = SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("nktkargo@gmail.com", "urzyuxbyvuratgud")
        mail.sendmail("Nurullah KARA", "nurullahkarailetisim@gmail.com", mesaj.encode("utf-8"))
    except:
        pass
    print(mesaj)

veriCek()
eskiDeprem = datetime.datetime(int(depremler[0][0:4]), int(depremler[0][5:7]), int(depremler[0][8:10]), int(depremler[0][11:13]), int(depremler[0][14:16]), int(depremler[0][17:19]))
yer = depremler[0][71:121].strip()
siddet = depremler[0][59:65].strip()
while(True):
    veriCek()
    karsilastir()
    time.sleep(1)