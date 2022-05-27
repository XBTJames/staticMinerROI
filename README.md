# staticMinerROI
Takes Data from Luxor's HashrateIndex API to return and chart static ASIC ROI.

Static ROI is calcuated by taking ASIC pricing (in USD per TH) and dividing by the USD hashprice on the day of the pricing, which returns the number of days needed for an ASIC to generate enough revneue to cover the upfront cost, before any other costs, assuming hashprice stays constant.

All data courtesy of HashrateIndex. Hashprice data: https://data.hashrateindex.com/network-data/btc ; ASIC pricing data: https://data.hashrateindex.com/asic-index-data

hashrateindex.py and resolvers.py come from the Hashrateindex API: https://github.com/LuxorLabs/hashrateindex-api-python-client
