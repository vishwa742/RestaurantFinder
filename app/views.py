from app import app
from flask import render_template, request, redirect
from app.yelp import yelp_search
import pandas as pd
from io import StringIO
import json
#from IPython.display import HTML


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req["username"]
        email = req["email"]
        password = req["password"]
        print(username, email, password)

        return redirect(request.url)

    return render_template("public/sign_up.html")


@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":

        search_req = request.form["search"]
        searching = search_req
        result = yelp_search(searching)
        # print(result)
        print(search_req)
        df = pd.DataFrame.from_dict(result, orient='index')

        reviews = result['Reviews']
        ratings = result['Rating']
        address = result['Address']
        phone = result['Phone']
        img_url = result['URL']

        return render_template('public/about.html', variable=result, reviews=reviews,
                               ratings=ratings, address=address, img_url=img_url, phone=phone)  # Dictionary

        # return(json.dump(result,indent = 6))

        # return render_template('public/about.html', variable=result  ) Dataframe

        # return render_template('public/simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

        # print(type(df))
        # return render_template('simple.html',  tables=[result.to_html(classes='data')], titles=df.columns.values)
        # return redirect(request.url)

    return render_template("public/search.html")
