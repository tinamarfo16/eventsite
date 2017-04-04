from flask import Flask
from flask import render_template
import eventbrite
import requests



app = Flask("MyApp")


@app.route("/")
def opening():

        return render_template('events.html')

        return "All OK"

@app.route("/results", methods=['POST'])
def results():


        endpoint = "https://www.eventbriteapi.com/v3/events/search/?token=C6HNAT657IPOB7635DXW"
        payload = { "q": "<name>", "q": "London,UK"}

        response =  requests.get(endpoint, params=payload)

        print response

        return render_template("results.html")


app.run()
