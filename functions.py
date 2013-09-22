#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameters import fields

def production(data, year, month, region, product_code, province = '' ):
    """Function that returns the volume production of a product in
       an specific month and region
    """
    volumen = 0

    for item in data:
        if province == '':
            if item[fields['ANHO']] == year and item[fields['DEPARTAMENTO']] == \
               region and item[fields['CODIGO_PRODUCTO']] == product_code:
                volumen += float(item[fields[month]])
        else:
            if item[fields['ANHO']] == year and item[fields['DEPARTAMENTO']] == \
                region and item[fields['PROVINCIA']] == province and \
               item[fields['CODIGO_PRODUCTO']] == product_code:
                volumen += float(item[fields[month]])

    return volumen

def product_source(data, product_code):
    """Function that returns the provinces and regions that provide the given
    product
    """

    sources = []

    for item in data:
        if item[fields['CODIGO_PRODUCTO']] == product_code:
            sources.append([item[fields['DEPARTAMENTO']],
            item[fields['PROVINCIA']]])

    return sources

def region_products(data, region, province=''):
    """Function that returns the products from a region or province
    """

    products = {}

    for item in data:
        if province != '':
            if item[fields['DEPARTAMENTO']] == region and \
                item[fields['PROVINCIA']]  == province:
                if not item[fields['CODIGO_PRODUCTO']] in products.keys():
                    products[item[fields['CODIGO_PRODUCTO']]] = \
                    item[fields['PRODUCTO']]
        else:
            if item[fields['DEPARTAMENTO']] == region:
                if not item[fields['CODIGO_PRODUCTO']] in products.keys():
                    products[item[fields['CODIGO_PRODUCTO']]] = \
                    item[fields['PRODUCTO']]

    return products

def product_region_percentages(data, year, product_code):
    """Function that returns the percentages of a product by region and
    province
    """

    percentages = []
    total_amount = 0

    # We add all the regions and provinces that produce the item with the
    # yearly amount of production and sums the amounts of production
    for item in data:
        if item[fields['ANHO']] == year and item[fields['CODIGO_PRODUCTO']] == product_code:
            percentages.append([item[fields['DEPARTAMENTO']],
                                item[fields['PROVINCIA']],
                                float(item[fields['TOTAL']])])
            total_amount += float(item[fields['TOTAL']])

    # We calculate the percentages of each province
    for item in percentages:
        item.append(round(item[2]/total_amount,5))

    return percentages

