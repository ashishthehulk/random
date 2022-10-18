import requests
import bs4
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}
# Make requests from webpage
url = 'https://www.digikey.in/en/products/filter/through-hole-resistors/53?s=N4IgTCBcDaIIwAYDWACATgUwM4EssBcB7NEAXQBoQBWKUAByjkrockQQF8Og'
result = requests.get(url,headers=headers)


# Creating soap object
soup = bs4.BeautifulSoup(result.text,'lxml')



# Searching div tags having maincounter-number class
cases = soup.find_all('tr' ,class_= 'MuiTableRow-root jss266')



# Lists to store number of data
dataID = []
dataName = []
prodName = []
dataPrice = []
dataCase = []
dataTemp = []

print(len(cases))
# Find the span and get data from it
for i in cases:
    spanID = i.find('a',{'class':'jss262 jss246'})
    dataID.append(spanID.string)
    spanName = i.find("div", {"class": "jss260"})
    dataName.append(spanName.string)
    spanProd = i.find('a',{'class':'jss261'})
    prodName.append(spanProd.string)
    spanCase = i.find('td',{'data-atag':'CLS 16'})
    dataCase.append(spanCase.string)
    spanPrice = i.find('td',{'data-atag':'tr-unitPrice'}).find('strong')
    dataPrice.append(spanPrice.string)
    spanTemp = i.find('td',{'data-atag':'CLS 252'})
    dataTemp.append(spanTemp.string)

df = pd.DataFrame({"Product ID": dataID,"Name":dataName,"Manufacturer":prodName,"Case/Package":dataCase,"Operating Temperature":dataTemp,"Price":dataPrice})




# # Exporting data into Excel
df.to_csv('digiKeyData.csv')
