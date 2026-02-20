import sys
import requests
from bs4 import BeautifulSoup

url=(sys.argv[1])
url_air_qual=(sys.argv[2])

#url ='https://www.accuweather.com/en/ir/tabriz/207308/current-weather/207308' 
#url_air_qual='https://www.accuweather.com/en/ir/tabriz/207308/air-quality-index/207308'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Waccu.py(KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Connection": "keep-alive",
}
try:
        def start(url,url_air_qual):
                response = requests.get(url, headers=headers)
                response_air_qual=requests.get(url_air_qual,headers=headers)
                response.raise_for_status()
                response_air_qual.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")
                soup_air_qual=BeautifulSoup(response_air_qual.text,"html.parser")

                temp=soup.find("div",class_='display-temp')
                detailed_data= soup.find("div", class_="detail-item spaced-content")
                city= soup.find("h1", class_="header-loc")
                phrase=soup.find("div", class_='phrase')
                air_qual=soup_air_qual.find("div", class_='aq-number')
                print("\nCity:", city.get_text(strip=True) if city else "Not found")
                print('\nTemperature:',temp.get_text(strip=True)if temp else "Not found")
                print(f"\nWeather condition: {phrase.get_text(strip=True) if phrase else 'Not found'}")
                print(f"\nAir quality: {air_qual.get_text(strip=True) if air_qual else 'Not found'} AQI")
                print(detailed_data.parent.get_text() if detailed_data else "Not found")
        
except ValueError:
            print(error)
start(url,url_air_qual)
