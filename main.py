from numpy import format_float_positional
import pandas as pd
from datetime import datetime
from CityLoader import CityLoader
from City import City

if __name__ == '__main__':
  cities = []
  cities.append(City('[{"id":60,"name":"Свердловская область","areaType": "Region","hasMetros": true,"hasDistricts": false,"HasRoads": false},{"id": 2653,"name": "Екатеринбург","areaType": "City","hasMetros": true,"hasDistricts": false,"HasRoads": false}]', 'Yekaterinburg'))

  cities.append(City('[{"id": 69,"name": "Калининградская область","areaType": "Region","hasMetros": false,"hasDistricts": false,"HasRoads": false},{"id": 2919,"name": "Калининград","areaType": "City","hasMetros": false,"hasDistricts": false,"HasRoads": false}]', 'Kaliningrad'))

  cities.append(City('[{"id": 3584,"name": "Москва","areaType": "City","hasMetros": true,"hasDistricts": false,"HasRoads": false}]', "Moscow"))

  cities.append(City('[{"id": 34,"name": "Якутия","areaType": "Region","hasMetros": false,"hasDistricts": false,"HasRoads": false},{"id": 1268,"name": "Нерюнгри","areaType": "City","hasMetros": false,"hasDistricts": false,"HasRoads": false},{"id": 1257,"name": "Чульман","areaType": "City","hasMetros": false,"hasDistricts": false,"HasRoads": false}]', 'Neryungri'))

  for city in cities:
    loader = CityLoader(city)
    loader.load()
    df = pd.DataFrame(loader.items)
    df.to_csv(f'{datetime.today().strftime("%Y-%m-%d")} {city.name}.csv')



  #ekb = City('[{"id":60,"name":"Свердловская область","areaType": "Region","hasMetros": true,"hasDistricts": false,"HasRoads": false},{"id": 2653,"name": "Екатеринбург","areaType": "City","hasMetros": true,"hasDistricts": false,"HasRoads": false}]', 'Yekaterinburg')
  #ekbLoader = CityLoader(ekb)
  #ekbLoader.load()
  #df = pd.DataFrame(ekbLoader.items)
  #df.to_csv(f'{datetime.today().strftime("%Y-%m-%d")} ekb.csv')
  
  #kln = City('[{"id": 69,"name": "Калининградская область","areaType": "Region","hasMetros": false,"hasDistricts": false,"HasRoads": false},{"id": 2919,"name": "Калининград","areaType": "City","hasMetros": false,"hasDistricts": false,"HasRoads": false}]', 'Kaliningrad')
  
  #klnLoader = CityLoader(kln)
  #klnLoader.load()
  #df = pd.DataFrame(klnLoader.items)
  #df.to_csv(f'{datetime.today().strftime("%Y-%m-%d")} kln.csv')
  