from app import app
from flask import render_template, request, redirect
from app.yelp import yelp_search
import pandas as pd
from io import StringIO
import json
#from IPython.display import HTML


@app.route("/", methods=["GET", "POST"])
def search():

    if request.method == "POST":

        search_req = request.form["search"]
        searching = search_req
        result = yelp_search(searching)
        print(search_req)
        df = pd.DataFrame.from_dict(result, orient='index')

        reviews = result['Reviews']
        ratings = result['Rating']
        address = result['Address']
        phone = result['Phone']
        img_url = result['URL']

        return render_template('public/about.html', variable=result, reviews=reviews,
                               ratings=ratings, address=address, img_url=img_url, phone=phone)  # Dictionary

    return render_template("public/search.html")


@app.route("/about")
def about():
    return render_template("public/about.html")
