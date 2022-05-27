# -*- coding: utf-8 -*-
"""
Author: @XBTJames
All data courtesy of Luxor's Hashrate Index. If attempting to replicate this analysis, you will need your own key, please reach out to the Luxor team at hashrateindex@luxor.tech

Hashprice data: https://data.hashrateindex.com/network-data/btc
ASIC Index data: https://data.hashrateindex.com/asic-index-data
"""
from hashrateindex import API
from resolvers import RESOLVERS
import pandas as pd
import matplotlib.pyplot as plt

API = API(host = 'https://api.hashrateindex.com/graphql', method = 'POST', key = 'KEY') #Here, replace the Key with your own key. Key "KEY" I highly doubt works.
RESOLVERS = RESOLVERS(df = True)

### Here, we pull the ASIC data from the HashrateIndex API., and then set up the dataframe the way we'd like it.
resASIC = API.get_asic_price_index('_1_YEAR', 'USD')
ASICdf = RESOLVERS.resolve_get_asic_price_index(resASIC)

resHashprice = API.get_hashprice('_1_YEAR', 'USD')
hashpricedf = RESOLVERS.resolve_get_hashprice(resHashprice)

ASICdf['time'] = pd.to_datetime(ASICdf['time'])
ASICdf = ASICdf.set_index('time')

hashpricedf['timestamp'] = pd.to_datetime(hashpricedf['timestamp'])
hashpricedf = hashpricedf.set_index('timestamp')

dates = ASICdf.index.to_list() #dates is just a list of datetimes for which we have ASIC pricing data. The days which we have ASIC pricing data seems slightly smaller than the days which we have Hashprice data
under38ROI = [] #create three empty lists where we 
_38to68ROI = []
above68ROI = []
i = 0
while i < len(dates): #loop through and calculate static ROI for each date we have, dividing price per TH by hashprice, resulting in the days to ROI assuming zero power/other costs.
    currenthashprice = hashpricedf.loc[dates[i]]['usdHashprice']
    currentunder38ROI = ASICdf.loc[dates[i]]['under38'] / currenthashprice
    current_38to68ROI = ASICdf.loc[dates[i]]['_38to68'] / currenthashprice
    currentabove68ROI = ASICdf.loc[dates[i]]['above68'] / currenthashprice
    under38ROI.append(currentunder38ROI)
    _38to68ROI.append(current_38to68ROI)
    above68ROI.append(currentabove68ROI)
    i+=1

#plot the results
plt.plot(dates, under38ROI, label = 'Under 38 J/TH ROI')
plt.plot(dates,_38to68ROI, label = '38 to 68 J/TH ROI')
plt.plot(dates, above68ROI, label = 'Above 68 J/TH ROI')
plt.xlabel("Date - All data courtesy of Luxor's Hashrate Index")
plt.ylabel('Static ROI (days)')
plt.legend()
plt.show()
