import http.client
import json

class CityLoader:
    def __init__(self, city) -> None:
        self.city = city
        self.items = []
        self.offset = 0

    def load(self):
        print(f'{self.city.name} is loading')
        while self.loadChunk():
            pass
        print(f'{self.city.name} was loaded')
    
    def loadChunk(self):
        conn = http.client.HTTPSConnection("api.domofond.ru")
        payload = f'{{"id":"1","jsonrpc":"2.0","method":"Item.SearchItemsV3","params":{{"meta":{{"platform":"web","language":"ru","token":"Ac6sMzUwocbZwp3CxMPs1c2C3tmjraysrKJ2tDHahdbO2lNTrK2Mrh5CmgeYoGTaGfTkZC7ixxH9MSXkSxQTsaOkNLd7qUU="}},"filters":{{"itemType":"Sale","propertyType":null,"priceFrom":null,"priceTo":null,"rooms":[],"apartmentMaterial":[],"constructionMaterial":[],"rentalRate":null,"floorFrom":null,"floorTo":null,"notLastFloor":null,"numberOfFloorsFrom":null,"numberOfFloorsTo":null,"distanceFromMetro":null,"itemSoldByType":[],"withPhotos":false,"withDeposit":null,"withCommission":null,"mapped":false,"apartmentSaleType":null,"searchText":null,"excludeSearchText":null,"houseDescription":[],"houseMaterial":[],"distanceToCityFrom":null,"distanceToCityTo":null,"plotAreaFrom":null,"plotAreaTo":null,"plotDescription":[],"commercialDescription":[],"constructionStage":null,"hasDevelopmentFinishing":null,"projectCompletionDateYearFrom":null,"projectCompletionDateYearTo":null,"developmentPropertyType":[],"isPartOfRenovationProgram":null,"publicationTimeRange":null,"maxCommissionPercentage":null,"floorAreaFrom":null,"floorAreaTo":null,"kitchenSizeFrom":null,"kitchenSizeTo":null,"livingSizeFrom":null,"livingSizeTo":null,"buildYearFrom":null,"buildYearTo":null,"geographicWindow":{{"topLeft":{{"latitude":85.00000000000000,"longitude":-170.00000000000000}},"bottomRight":{{"latitude":-65.00000000000000,"longitude":170.00000000000000}}}},"geographicPolygon":null,"locations":{self.city.locations},"regionId":null,"cityIds":[],"districtIds":[],"stationIds":[],"roadIds":[],"adminDistrictIds":[]}},"order":"Default","offset":{200 * self.offset},"limit":200,"thumbnailUrlSize":{{"width":508,"height":373}}}}}}'
        headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,ru-RU;q=0.9,ru;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain',
        'Cookie': 'dfuid=232bb6a3-706f-45ea-8521-6b2f8407b2e6; rrpvid=753335777390428; duid=U7oNVSgtESZhbukWOQkNPYU0WC9hWfa8PvRTLP3Oq6HQk2J3',
        'DNT': '1',
        'Origin': 'https://www.domofond.ru',
        'Referer': 'https://www.domofond.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
        }

        conn.request("POST", "/rpc", payload.encode('utf-8'), headers)
        res = conn.getresponse()
        response = res.read()
        responseJson = self.convertToJson(response.decode("utf-8"))
        pagesCount = responseJson['result']['totalPages']
        totalCount = responseJson['result']['totalCount']
        if pagesCount > self.offset:
            self.offset += 1
            self.items.extend([self.convertRowToJson(row) for row in responseJson['result']['items']])
            print(f'{self.offset} of {pagesCount}. {len(self.items)} of {totalCount}')
            return True
        else:
            return False

    def convertToJson(self, text):
        return json.loads(text)
    
    def convertRowToJson(self, row):
        result = (row['dataSummary'])
        result['id'] = row['id']
        return result