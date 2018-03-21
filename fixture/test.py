#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import json
import requests

url = 'http://127.0.0.1:8520/SHSRC/MI/TSM/1/1/PutApduScripts'
data = {
    'apduType':'person',
    'cardLinkingInfo':'afajgekgh465433334sa131',
    'scriptsInstanceId':'112233445566778899',
    'xmTransNum':'112233445566',
    'xmTransTime':'123456789985',
    'spTransNum':'112233445566',
    'spTransTime':'14564852341',
    'apduModelList':[{'apdu':'00A404000EA0000003B0414D53442053425400','expStatusRegEx':'.*9000$'},
                     {'apdu':'805020000861763E10DD444246','expStatusRegEx':'.*9000$'},
                     {'apdu':'8482330010D4EC214747FDB7BF1765AAA939FB2859','expStatusRegEx':'.*9000$'},
                     {'apdu':'84D8318146318811108F70DEBACA6C417A22FE76A84869E25603D04A3C881110A6BDE3721FEBC4D1ACB6C5587BB41FB903D3C63D881110A597FD053444A471DD2A13346C4529E7033780A0','expStatusRegEx':'.*9000$'},
                     {'apdu': '84E22001CADF0220A4BB109EBFCA7591935E8F36D95490FB08D6EEA01BBCAA2B7FC95568F8AA59A6DF03205E8276CA1806D0C65EC716DF269095899C4CB442B74EA3BEA8B00B116445BA6CDF04020001DF102049B31F3C6A4959C1366D7DA0773EB291D7EB9C1F8ED991652131D629D47AA45EDF112088290BA3663835C0672B65974EC37EFD8519579B61997933944B0DB5886A9F2ADF12208093CDF90DE7EED4B14449961BAE8DEB5711292591A4DE7ABECED58267A64762DF131361114F09A00000000386980701500450424F43', 'expStatusRegEx': '.*9000$'},
                     {'apdu': '805020000861763E10DD444246', 'expStatusRegEx': '.*9000$'}],


}

# for cmd in data['apduModelList']:
#     print(cmd)
#     apdu = cmd['apdu']
#     print(apdu)

req = json.dumps(data)

res = requests.post(url,req)
print(res.content)