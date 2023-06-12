# import joblib
# from flask import Flask, render_template, request, jsonify
# from flask_cors import cross_origin

# app = Flask(__name__, template_folder="template")

# # Load model from model.pkl
# model = joblib.load('model.pkl')

# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=['Get','POST'])
# @cross_origin()
# def predict():
#     if request.method == "POST":
#         temperature = float(request.form['Temperature'])
#         pressure = float(request.form['Pressure'])
#         humidity = float(request.form['Humidity'])
#         windDirection = float(request.form['WindDirection'])
#         speed = float(request.form['Speed'])
#         dayOfYear = float(request.form[])
#         timeOfDay = float(request.form['TimeOfDay_s'])



#         radiation_amount = round(model.predict([[temperature, pressure, humidity, windDirection, speed, dayOfYear, timeOfDay]])[0], 2)

#         # Pass the radiation_amount to the template
#         return render_template("predictor.html", radiation_amount=radiation_amount)
#     else:
#         return render_template("predictor.html")


# if __name__ == "__main__":
#     app.run(debug=True)

# import joblib
# from flask import Flask, render_template, request, jsonify
# from flask_cors import cross_origin
# from datetime import datetime

# app = Flask(__name__, template_folder="template")

# # Load model from model.pkl
# model = joblib.load('model.pkl')

# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=['Get','POST'])
# @cross_origin()
# def predict():
#     if request.method == "POST":
#         temperature = float(request.form['Temperature'])
#         pressure = float(request.form['Pressure'])
#         humidity = float(request.form['Humidity'])
#         windDirection = float(request.form['WindDirection_D'])
#         speed = float(request.form['Speed'])
#         # dayOfYear = datetime(request.form['DayOfYear'])
#         # timeOfDay = datetime(request.form['TimeOfDay_s'])

#         # date_object = datetime.strptime(dayOfYear, "%Y-%m-%d")

#         # time_object = datetime.strptime(timeOfDay, '%H:%M')
#         dayOfYear = int(request.form['DayOfYear'])
#         timeOfDay = request.form['TimeOfDay_s']

#         # Convert dayOfYear to datetime object
#         date_object = datetime.strptime(dayOfYear, '%Y-%m-%d')
#         time_object = datetime.strptime(timeOfDay, '%H:%M')

       

#         radiation_amount = round(model.predict([[temperature, pressure, humidity, windDirection, speed, date_object , time_object]])[0], 2)

#         # Pass the radiation_amount to the template
#         return render_template("predictor.html", radiation_amount=radiation_amount)
#     else:
#         return render_template("predictor.html")


# if __name__ == "__main__":
#     app.run(debug=True)

# import joblib
# from flask import Flask, render_template, request, jsonify
# from flask_cors import cross_origin
# from datetime import datetime

# app = Flask(__name__, template_folder="template")

# # Load model from model.pkl
# model = joblib.load('model.pkl')

# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=['GET','POST'])
# @cross_origin()
# def predict():
#     if request.method == "POST":
#         temperature = float(request.form['Temperature'])
#         pressure = float(request.form['Pressure'])
#         humidity = float(request.form['Humidity'])
#         windDirection = float(request.form['WindDirection_D'])
#         speed = float(request.form['Speed'])
#         dayOfYear = request.form['DayOfYear']
#         timeOfDay = request.form['TimeOfDay_s']

#         # Convert dayOfYear to datetime object
#         date_object = datetime.strptime(dayOfYear, '%Y-%m-%d')
#         # Extract the day of the year
#         day_of_year = date_object.timetuple().tm_yday

#         radiation_amount = round(model.predict([[temperature, pressure, humidity, windDirection, speed, day_of_year, timeOfDay]])[0], 2)

#         # Pass the radiation_amount to the template
#         return render_template("predictor.html", radiation_amount=radiation_amount)
#     else:
#         return render_template("predictor.html")


# if __name__ == "__main__":
#     app.run(debug=True)

# import joblib
# from flask import Flask, render_template, request, jsonify
# from flask_cors import cross_origin
# from datetime import datetime

# app = Flask(__name__, template_folder="template")

# # Load model from model.pkl
# model = joblib.load('model.pkl')

# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=['GET','POST'])
# @cross_origin()
# def predict():
#     if request.method == "POST":
#         temperature = float(request.form['Temperature'])
#         pressure = float(request.form['Pressure'])
#         humidity = float(request.form['Humidity'])
#         windDirection = float(request.form['WindDirection_D'])
#         speed = float(request.form['Speed'])
#         dayOfYear = request.form['DayOfYear']
#         timeOfDay = request.form['TimeOfDay_s']

#         # Convert dayOfYear to datetime object
#         date_object = datetime.strptime(dayOfYear, '%Y-%m-%d')
#         # Extract the day of the year
#         day_of_year = date_object.timetuple().tm_yday

#         radiation_amount = round(model.predict([[temperature, pressure, humidity, windDirection, speed, day_of_year, timeOfDay]])[0], 2)

#         # Pass the radiation_amount to the template
#         return render_template("predictor.html", radiation_amount=radiation_amount)
#     else:
#         return render_template("predictor.html")


# if __name__ == "__main__":
#     app.run(debug=True)

import joblib
from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin
from datetime import datetime

app = Flask(__name__, template_folder="template")

# Load model from model.pkl
model = joblib.load('model.pkl')

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        temperature = float(request.form['Temperature'])
        pressure = float(request.form['Pressure'])
        humidity = float(request.form['Humidity'])
        windDirection = float(request.form['WindDirection_D'])
        speed = float(request.form['Speed'])
        dayOfYear = request.form['DayOfYear']
        timeOfDay = request.form['TimeOfDay_s']

        # Convert dayOfYear to datetime object
        date_object = datetime.strptime(dayOfYear, '%Y-%m-%d')
        # Extract the day of the year
        day_of_year = date_object.timetuple().tm_yday

        # Convert timeOfDay to minutes since midnight
        hours, minutes = map(int, timeOfDay.split(':'))
        time_in_minutes = hours * 60 + minutes

        radiation_amount = round(model.predict([[temperature, pressure, humidity, windDirection, speed, day_of_year, time_in_minutes]])[0], 2)

        # Pass the radiation_amount to the template
        return render_template("predictor.html", radiation_amount=radiation_amount)
    else:
        return render_template("predictor.html")


if __name__ == "__main__":
    app.run(debug=True)
