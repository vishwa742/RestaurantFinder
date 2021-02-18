import requests as r
import numpy as np
import pandas as pd
from itertools import product

from flask import jsonify
from io import StringIO

import json
import sys

url = 'https://api.yelp.com/v3/businesses/search'
key = '5kC0LrgiGbVAwaMO_vyhpWvzZzVZ8GQanpgcON970i3XKkuofagqXet5US6ls0E1SLE6TTxUzDY95SqPpQTk-L_8tjOn_NYM4pgE_NcGytTAzy1lSqBilNgN5xUbYHYx'
headers = {
    'Authorization': 'Bearer %s' % key
}

def yelp_search(input):
    addresses = [input]
    #addresses = ['Kearny, New Jersey','Harrison, New Jersey']

    offset =np.arange(0,500,50)

    tuples = list(product(addresses,offset))
    tuples[:5]

    listing = []

    cols = ['Name','Reviews','Rating','Address','Phone','URL']

    for address,step in tuples:
        search_parameters = {
        "location":address,
        "limit":50,
        "term":'',
        "radius":805,
        "offset":step
        }

        resp = r.get(url,headers=headers, params=search_parameters)
        raw_data = resp.json()
        for business in raw_data['businesses']:
            name = business['name']
            reviews = business['review_count']
            rating = business['rating']
            location = business['location']['display_address'][0]
            phone = business['display_phone']
            img_url = business['image_url']
            listing.append([name,reviews,rating,location,phone,img_url])
        df = pd.DataFrame.from_records(listing, index='Name', columns=cols)
        #df=df.head()
        dictionary = df.to_dict()
        

    return(dictionary)
  



