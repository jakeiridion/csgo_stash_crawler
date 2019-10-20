import requests
from bs4 import BeautifulSoup
import time

while True:
    skins = []
    url = input("Enter Skin URL\n> ")
    if url == "q":
        break
    title = ""


    class CrawledSkin():
        def __init__(self, name, quality, stattrack, souvenir, price, stattrack_price, souvenir_price):
            self.name = name
            self.quality = quality
            self.stattrack = stattrack
            self.souvenir = souvenir
            self.price = price
            self.stattrack_price = stattrack_price
            self.souvenir_price = souvenir_price


    class Fetcher():
        def fetch(self):
            a = 0

            time.sleep(1)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            global title
            title = soup.select_one("h1").text

            for skin in soup.find_all("div", attrs={"class": "well result-box nomargin"}):
                # name

                if skin.select_one("h3") is not None:
                    name = skin.select_one("h3").text
                elif skin.select_one("h3") is None and a == 0:
                    a = 1
                    continue
                else:
                    name = "None"

                # quality

                if skin.find("p") is not None:
                    quality = skin.find("p").text.strip()
                else:
                    quality = "None"

                # stattrack

                if skin.select_one(".stattrak") is not None:
                    stattrack = skin.select_one(".stattrak").text.strip()
                else:
                    stattrack = "None"

                # souvenir

                if skin.select_one(".souvenir") is not None:
                    souvenir = skin.select_one(".souvenir").text.strip()
                else:
                    souvenir = "None"

                # price

                if skin.select_one(".price") is not None:
                    price = skin.select_one(".price").text.strip()
                else:
                    price = "None"

                # stattrack_price

                if skin.select_one(".price-st") is not None:
                    stattrack_price = skin.select_one(".price-st").text.strip()
                else:
                    stattrack_price = "None"

                # souvenir_price

                if skin.select_one(".price-souv") is not None:
                    souvenir_price = skin.select_one(".price-souv").text.strip()
                else:
                    souvenir_price = "None"

                crawled = CrawledSkin(name, quality, stattrack, souvenir, price, stattrack_price, souvenir_price)
                skins.append(crawled)

        def write(self):
            with open(str(title) + ".csv", "w") as csvfile:
                csvfile.write("Name:,Rarity:,Stattrack:,Souvenir:,Price:,Stattrack Price,Souvenir Price:\n")
                for skin in skins:
                    csvfile.write(
                        '"' + skin.name + '","' + skin.quality + '","' + skin.stattrack + '","' + skin.souvenir + '","' + skin.price + '","' + skin.stattrack_price + '","' + skin.souvenir_price + '"\n')


    f = Fetcher()
    f.fetch()
    f.write()
    print("Creating file")
    print("...")
    print("")