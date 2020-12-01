import requests
import json

class Compinfor:
    def __init__(self, taxid):
        self.texid = taxid

    def getinfo(self):
        url = "https://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO%20eq%20" + \
              str(self.texid) + "&$skip=0&$top=50"
        session = requests.Session()
        response = session.get(url)
        output = json.loads(response.text)


        return output

    def __str__(self):
        print(self.texid)

