
from flask import Flask, request, jsonify,render_template
from covid import Covid
from covid_india import states
from datetime import datetime
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
     covid = Covid(source="worldometers")
     country = "India"
     active = covid.get_total_active_cases()
     confirmed = covid.get_total_confirmed_cases()
     recovered = covid.get_total_recovered()
     deaths = covid.get_total_deaths()
     data = covid.get_status_by_country_name(country)
     return render_template('index.html',data=data,active=active,confirmed=confirmed,recovered=recovered,deaths=deaths)


@app.route('/country/',methods=["POST"])
def search_country():
    if request.method == 'POST':
        covid = Covid(source="worldometers")
        country = request.form['country']
        active = covid.get_total_active_cases()
        confirmed = covid.get_total_confirmed_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()
        data = covid.get_status_by_country_name(country)   
        return render_template('index.html',data=data,active=active,confirmed=confirmed,recovered=recovered,deaths=deaths)


@app.route('/country/state/',methods=["POST"])
def search_state():
    if request.method == 'POST':
        state = request.form['state']
        data = states.getdata(state)
        covid = Covid(source="worldometers")
        active = covid.get_total_active_cases()
        confirmed = covid.get_total_confirmed_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()
        return render_template('index.html',data=data,state=state,active=active,confirmed=confirmed,recovered=recovered,deaths=deaths)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)



