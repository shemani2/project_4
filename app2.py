from flask import Flask, request, render_template, flash
import pickle
from markupsafe import Markup
import os

app = Flask(__name__)

# Set secret keys for Flask application
app.secret_key = "grey"

# Homepage
@app.route("/")
def index():
    return render_template('index_1.html')

# Result page
@app.route("/output", methods=["POST", "GET"])
def output():
    if request.method == 'POST':
        try:
            # gender
            g = request.form['gender']
            if g == "male":
                g = 1
            elif g == "female":
                g = 0
            else:
                raise ValueError("Invalid gender value")
                
            # age
            a = request.form.get('age')
            if not a:
                raise ValueError("Age is required")
            a = int(a)
            a = (a - 0) / (110 - 0)
            
            # hyper-tension
            hyt = request.form['hypertension'].lower()
            hyt = 1 if hyt == "yes" else 0
            
            # heart-disease
            ht = request.form['heart-disease'].lower()
            ht = 1 if ht == "yes" else 0
            
            # residency-type
            r = request.form['residency'].lower()
            if r not in ["urban", "rural"]:
                raise ValueError("Invalid residency value")
            r = 1 if r == "urban" else 0
            
            # glucose-levels
            gl = request.form.get('glucose')
            if not gl:
                raise ValueError("Glucose level is required")
            gl = int(gl)
            gl = (gl - 50) / (300 - 50)
            
            
            # smoking
            s = request.form['smoking'].lower()
            smoking_map = {
                "smokes": 1,
                "never smoked": 0,
            }
            s = smoking_map.get(s)
            if s is None:
                raise ValueError("Invalid smoking status value")

            # Make prediction
            prediction = stroke_pred(g, a, hyt, ht, r, gl, s)
            return render_template('index_2.html', prediction_html=prediction)
        except ValueError as e:
            return f"Invalid input: {e}"
        except Exception as e:
            return f"An error occurred: {e}"

def stroke_pred(g, a, hyt, ht, r, gl, s):
    try:
        # Debugging print statement for current working directory
        print(f"Current working directory: {os.getcwd()}")
        
        # Debugging print statement for model file path
        model_path = 'model.pkl'
        print(f"Model file path: {model_path}")
        
        # Load model
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        # User input
        user_input = (g, a, hyt, ht, r, gl, s)
        decoded_user_input = fancy_deconstruct(user_input)
        
        # Debugging print statement
        print(f"Decoded user input: {decoded_user_input}")
        
        # Predictions
        result = model.predict([decoded_user_input])[0]
        
        # Debugging print statement
        print(f"Prediction result: {result}")
        
        # Output
        if result == 1:
            return Markup("Patient is at risk of stroke. <br> Please seek professional medical care for preventative measures.")
        else:
            return Markup("No risk of stroke detected. <br> Please continue monitoring patient's health and well-being.")
    except Exception as e:
        return f"An error occurred while making the prediction: {e}"

# Deconstruct and encode inputs, transform 10 columns to 20
def fancy_deconstruct(user_input):
    try:
        g, a, hyt, ht, r, gl, s = user_input
        g_female, g_male = (0, 0)
        if g == 0:
            g_female = 1
        else:
            g_male = 1

        r_urban, r_rural = (0, 0)
        if r == 1:
            r_urban = 1
        else:
            r_rural = 1

        s_never, s_yes = (0, 0)
        if s == 0:
            s_never = 1
        elif s == 1:
            s_yes = 1

        # Decoded input
        decoded_input = [a, hyt, ht, gl,  g_female, g_male,
                         r_rural, r_urban, s_never, s_yes]
        return decoded_input
    except Exception as e:
        raise ValueError(f"Error in fancy_deconstruct: {e}")

if __name__ == '__main__':
    app.run(debug=True)
