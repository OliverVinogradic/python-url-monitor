import urllib.request
import urllib.error

Websitentext = "websites.txt"

try:
    with open(Websitentext,"r",encoding="utf-8") as Urls:


        for Zeile in Urls:
            Zeile = Zeile.strip()

            try:

              ping = urllib.request.urlopen(Zeile, timeout=5)

              if ping.status == 200:
                print(Zeile+" Erreichbar")

            except urllib.error.URLError:
                    print(Zeile+" Urls konnte nicht gefunden werden oder ist down.")

            except Exception as e:
             print(e)



except FileNotFoundError:
    print("File could not be found")
