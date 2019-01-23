# -*-  coding: UTF-8 -*-
import sys
import os
import requests


latitude = '55.43'
longitude = '12.31'
radius = '15000'
title = 'Fantastiske fanadisqe favorittilbud'

with open('list.txt') as file:
    queries = file.read().splitlines()

loop = ""
for typevare in queries:
    url = 'https://api.etilbudsavis.dk/v2/offers/search?r_lat='+latitude+'&r_lng='+longitude+'&r_radius='+radius+'&r_locale=da_DK&api_av=0.3.0&query='+typevare+'&offset=0&limit=24'

    r = requests.get(url)
    varer = r.json()


    for vare in varer:
        fradato = vare['run_from'].split('T')[0]
        tildato = vare['run_till'].split('T')[0]

        linje = """
<div style='display:inline-block; margin:15px;background-color:#ddd;'>
    <div style='display:inline-block;'>
        <a href='https://etilbudsavis.dk/offers/%s'>
            <img src='%s'>
        </a>
    </div>
    <div style='display:inline-block;'>
        <h2> %s </h2> <br>
        <gray> %s </gray> <br>
        <strong> %s kr. </strong> <br>
        %s <br> <br>
        <gray> Tilbuddet gælder: <br>
        fra %s <br>
        til %s <br>
        <gray>
    </div>
</div>
<br>
""" % (
            vare['id'],
            vare['images']['view'],
            vare['heading'],
            vare['description'],
            vare['pricing']['price'],
            vare['branding']['name'],
            fradato,
            tildato)
        loop = loop + linje


html_kode1 = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>%s</title>

<style> 
gray {color:#666666;}
</style>

</head>

<body>
""" % (title,)



html_kode2 = "</body> </html>"

html_kode = html_kode1 + loop + html_kode2

filhtml = open('index.html', 'w')
filhtml.write(html_kode)
filhtml.close()
