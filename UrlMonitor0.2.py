import urllib.request
import urllib.error

Websitentext = "websites.txt"

try:
    with open(Websitentext,"r",encoding="utf-8") as Urls:


        for Zeile in Urls:
            Zeile = Zeile.strip()

            try:
                
                anfrage = urllib.request.Request(
                    Zeile, 
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                )
                
                
                ping = urllib.request.urlopen(anfrage, timeout=7) # Timeout auf 7 Sekunden erhöht

                if ping.status == 200:
                    print(Zeile + " -> Erreichbar")

            except urllib.error.HTTPError as fehler:
                
                print(f" {Zeile} -> Server-Fehler: {fehler.code}")
                
            except urllib.error.URLError:
                print(Zeile + " -> Url konnte nicht gefunden werden.")

            except Exception as e:
                print(f" {Zeile} -> Anderer Fehler: {e}")



except FileNotFoundError:
    print("File could not be found")
