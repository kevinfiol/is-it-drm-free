import requests

class ITAD:
    def __init__(self, base_url, api_key, region, country):
        self.base_url = base_url
        self.api_key = api_key
        self.region = region
        self.country = country
        self.shops = self.getStoresInRegion(region, country)

    def makeEndpoint(self, version, iface, method):
        return f'{self.base_url}/{version}/{iface}/{method}/'

    # https://itad.docs.apiary.io/#reference/search/search/find-games
    def search(self, name):
        endpoint = self.makeEndpoint('v02', 'search', 'search')
        params = {
            'key': self.api_key,
            'q': name,
            'limit': 15,
            'strict': 1
        }

        res = requests.get(endpoint, params=params)
        return res.json()

    # https://itad.docs.apiary.io/#reference/game/prices/get-current-prices
    def getPrices(self, plain_id):
        endpoint = self.makeEndpoint('v01', 'game', 'prices')
        params = {
            'key': self.api_key,
            'plains': plain_id,
            'shops': self.shops,
            'region': self.region,
            'country': self.country
        }

        def filterFn(x):
            return (x['shop']['id'] == 'itchio') or ('DRM Free' in x['drm'])

        res = requests.get(endpoint, params=params)
        data = res.json()['data'][plain_id]['list']
        drm_free_prices = list(filter(filterFn, data))
        return { 'data': drm_free_prices }

    def getStoresInRegion(self, region, country):
        endpoint = self.makeEndpoint('v02', 'web', 'stores')
        params = {
            'key': self.api_key,
            'region': region,
            'country': country
        }

        res = requests.get(endpoint, params=params)
        data = res.json()['data']
        stores = list(map(lambda x: x['id'], data))
        storeString = ','.join(stores)
        return storeString
