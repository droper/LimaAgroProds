#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from junar import ApiClient

from functions import production, product_source, region_products, \
product_region_percentages
from parameters import GUID, AUTH_KEY, fields

junar_api_client = ApiClient(AUTH_KEY)
datastream = junar_api_client.datastream(GUID)
data = datastream.invoke(output = 'json_array')

#print production(data['result'][1:], '2008', 'MAR', 'ANCASH', '0201')
#print product_source(data['result'][1:], '0201')
#print region_products(data['result'][1:], 'AREQUIPA')
print  product_region_percentages(data['result'][1:], '2012', '3802')


