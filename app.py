from flask import Flask,request,render_template
from covid import Covid
from covid_india import states
from datetime import datetime

 
app = Flask(__name__)
 
@app.route('/')

def home_view(): 
        return "<h1>Welcome to Geeks for Geeks</h1>"

def home():
     covid = Covid(source="worldometers")
     country = "India"
     active = covid.get_total_active_cases()
     confirmed = covid.get_total_confirmed_cases()
     recovered = covid.get_total_recovered()
     deaths = covid.get_total_deaths()
     data = covid.get_status_by_country_name(country)
     print(data)
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

if __name__== '__main__':
    app.run(debug=True)
