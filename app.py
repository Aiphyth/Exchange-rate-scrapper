from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import style
import datetime
import json


def parseTable(date):
    html2 = urlopen("http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.jsp?date=" + date)
    soup = BeautifulSoup(html2, 'lxml')
    tableToParse = soup.find("table", class_="kurzy_tisk")
    data = []
    rows = tableToParse.findAll('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data


style.use("ggplot")
dnes = datetime.datetime.today().date()
vcera = dnes - datetime.timedelta(days=1)
predevcirem = vcera - datetime.timedelta(days=1)
#html = urlopen("http://www.cnb.cz/cs/index.html")
dnes = str(dnes.day)+"."+str(dnes.month)+"."+str(dnes.year)
vcera = str(vcera.day)+"."+str(vcera.month)+"."+str(vcera.year)
predevcirem = str(predevcirem.day)+"."+str(predevcirem.month)+"."+str(predevcirem.year)

datum = [predevcirem,vcera,dnes]
EUR = []
USD = []
GBP = []


for day in datum:
    result = parseTable(day)
    euro = result[6][4]
    euro = euro.replace(",", ".")
    euro = float(euro)
    dolar = result[32][4]
    dolar = dolar.replace(",", ".")
    dolar = float(dolar)
    libra = result[33][4]
    libra = libra.replace(",", ".")
    libra = float(libra)
    USD.append(dolar)
    EUR.append(euro)
    GBP.append(libra)

kurzy = [EUR,USD,GBP]
with open("data.json", "w") as file:
    json.dump(kurzy, file)


'''
EUR = soup.find(id="rate_eur").text
USD = soup.find(id="rate_usd").text
GBP = soup.find(id="rate_gbp").text

EUR = EUR.replace(",", ".")
EUR = float(EUR)

USD = USD.replace(",", ".")
USD = float(USD)

GBP = GBP.replace(",", ".")
GBP = float(GBP)


plt.plot(datum, EUR,"g", label="EUR")
plt.plot(datum, USD,"r", label="USD")
plt.plot(datum, GBP, "b", label="GBP")

plt.title("Vývoj kurzu měn:")
plt.ylabel("Cena měny v CZK")
plt.xlabel("Datum")

plt.legend()

plt.show()
'''

a




