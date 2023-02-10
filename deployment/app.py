from flask import Flask, request, render_template
import pickle
import joblib

app = Flask(__name__)

# models for predicting house or apartment price with city name

model_house = joblib.load('/gb_regressor.pkl')
model_apartment = joblib.load('/rf_regressor.pkl')
# model to predict house price

@app.route('/', methods =["GET", "POST"])
def input():
    if request.method == "POST":
       # getting input from HTML form
       input_type = request.form.get("region")
       input_zip = request.form.get("number_of_rooms")
       input_area = request.form.get("living_area")
       input_garden = request.form.get("garden")
       input_terrace = request.form.get("terrace")
       input_type = request.form.get("state_of_the_building")
       input_zip = request.form.get("swimming_pool")
       input_area = request.form.get("open_fire")
       input_garden = request.form.get("garden")
       input_terrace = request.form.get("kitchen")
       

       return 
    return render_template("predict_house.html")

if __name__ == '__main__':
   app.run(debug = True)
    
