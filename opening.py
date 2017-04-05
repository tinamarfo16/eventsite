from flask import Flask
from flask import render_template, request
import eventbrite
import requests




app = Flask("MyApp")


@app.route("/")
def opening():

        return render_template("events.html")

        return "All OK"

@app.route("/results", methods=['POST'])
def results():


        endpoint = "https://www.eventbriteapi.com/v3/events/search/?token=C6HNAT657IPOB7635DXW"
        payload = {"q": "London,UK"}
        response =  requests.get(endpoint, params=payload)

        #print response
        #print response.json()
        event_names=[]
        for event in response.json()['events']:
            event_names.append({"name":event['name']['text'], "id":event['id']})

            print "its {place}".format(
            place=event['id']
            )

        #print response.json()['events'][0]

        return render_template("results.html", results= event_names)
        return "All OK"



@app.route("/results", methods=['GET'])
def checkbox():

    value = request.form.getlist('id')
    print value

    return '''<form method="post">
            <input type="checkbox" name="hello" value="id" checked>
            <input type="submit">
            </form>'''
#   return render_template("thankyou.html")
    return "All OK"


@app.route("/thankyou")
def hello():
        return render_template("emailtemp.html")

#@app.route("/sent", methods=['POST'])
#def sent():



app.run()
