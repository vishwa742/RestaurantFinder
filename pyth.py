import requests as r
import numpy as np
import pandas as pd
from itertools import product

import json
import sys

url = 'https://api.yelp.com/v3/businesses/search'
key = '5kC0LrgiGbVAwaMO_vyhpWvzZzVZ8GQanpgcON970i3XKkuofagqXet5US6ls0E1SLE6TTxUzDY95SqPpQTk-L_8tjOn_NYM4pgE_NcGytTAzy1lSqBilNgN5xUbYHYx'
headers = {
    'Authorization': 'Bearer %s' % key
}

def show():
    #x = input('Enter a place: ')
    #addresses = [x]
    addresses = ['Kearny, New Jersey','Harrison, New Jersey']

    offset =np.arange(0,500,50)

    tuples = list(product(addresses,offset))
    tuples[:5]

    listing = []

    cols = ['Name','Reviews','Rating','Address','Phone']

    for address,step in tuples:
        search_parameters = {
        "location":address,
        "limit":50,
        "term":'free wifi',
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
            listing.append([name,reviews,rating,location,phone])
        df = pd.DataFrame.from_records(listing, index='Name', columns=cols)

    #df = df.to_dict()
    
    return(df.to_string())
    #return type(df)
#df = df.to_json() 
#gf = df.sort_values(by='Reviews',ascending=False)
#gf = gf.drop_duplicates()
#gf.head()
#print(gf.head())

#resp = {
#    "Response":200,
#    "Message":"Data from Py",
#   "Data":df
#}

#print(json.dumps(resp))

#sys.stdout.flush()