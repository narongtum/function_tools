import re
import httplib

stockDict={}
AssetsList = []

conn = httplib.HTTPSConnection("www.set.or.th")

# Liabilities = debt
# Assets
# Equity = the value of the shares issued by a company.

ventureName = "CHOTI"

http = "/set/companyhighlight.do?symbol="
http += "%s" %ventureName
http += "&ssoPageId=5&language=en&country=TH"




print http

conn.request("GET", http)
r1 = conn.getresponse()
#print r1.status, r1.reason


# Delete pattern 	<.*?>, 		nbsp,		 &;&
data1 = r1.read()
data1 = re.sub("<.*?>", "", data1)
data1 = re.sub("nbsp", "", data1)
data1 = re.sub("&;&;", "", data1)
data1 = re.sub("&;", "", data1)



# replace newline stript space
data = data1.replace('\n', '')

# if found the followering name of this 
# replace Assets with newline of Assets name
data = data.replace('Financial Data', '\n\n\nFinancial Data')
data = data.replace('Assets', '\nAssets')
data = data.replace('Liabilities', '\nLiabilities')
data = data.replace('Equity', '\nEquity')
data = data.replace('Paid-up Capital', '\nPaid-up Capital')
data = data.replace('Revenue', '\nRevenue')
data = data.replace('Net Profit', '\nNet Profit')
data = data.replace('EPS (Baht)', '\nEPS (Baht)')
data = data.replace('Financial Ratio', '\nFinancial Ratio')
data = data.replace('ROA(%)', '\nROA(%)')
data = data.replace('ROE(%)', '\nROE(%)')
data = data.replace('Net Profit Margin(%)', '\n\n\nNet Profit Margin(%)')


#print data

p = re.compile(r'(Assets.*)', re.IGNORECASE)
assetData = p.search(data)
if assetData:
			assetData = assetData.group(1)
			#print assetData



p = re.compile(r'(Liabilities.*)', re.IGNORECASE)
liabData = p.search(data)
if liabData:
			liabData = liabData.group(1)
			#print liabData


p = re.compile(r'(Equity.+)', re.IGNORECASE)
equityData = p.search(data)
if equityData:
			equityData = equityData.group(1)
			#print equityData
else:
    print 'data not found'


conn.close()


assetData = assetData.replace(' ','')   # get rid of space
assetData = assetData.replace('Assets','')  
assetData = assetData.split()

for each in assetData:
    AssetsList.append(each)
    # append to dict
    stockDict['Assets'] = AssetsList



AssetsList = []
liabData = liabData.replace(' ','')
liabData = liabData.replace('Liabilities','')
#print liabData
# strip get rid of whitespace
liabData = liabData.split()





for each in liabData:
    AssetsList.append(each)
    stockDict['Liabilities'] = AssetsList

AssetsList = []
equityData = equityData.replace(' ','')
equityData = equityData.replace('Equity','')

# strip get rid of whitespace
equityData = equityData.split()


for each in equityData:
    AssetsList.append(each)
    stockDict['Equity'] = AssetsList

print stockDict 

# Write to XML or sheet something