from flask import Flask, render_template, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Load CSV data
nutrition_data = pd.read_csv('nutrition.csv', index_col=0)
intakes_data = pd.read_csv('intakes.csv', index_col=0)

# Transpose nutrition_data
nutrition_data = nutrition_data.T

# Drop unnamed columns from intakes_data
intakes_data = intakes_data.loc[:, ~intakes_data.columns.str.contains('^Unnamed')]

# Default values
selected_age_gender = None
selected_food = None
servings = 1

@app.route('/')
def index():
    global selected_age_gender, selected_food, servings

    # Check if nutrition_data is defined
    nutrition_data_json = nutrition_data.to_json() if 'nutrition_data' in globals() else None

    # Pass data to the template
    return render_template('index.html', nutrients=nutrition_data.index, age_genders=intakes_data.columns[1:],
                        selected_age_gender=selected_age_gender, selected_food=selected_food, servings=servings,
                        foods=nutrition_data.columns, intakes_data=intakes_data.to_json(), nutrition_data=nutrition_data_json)

@app.route('/update_selection', methods=['POST'])
def update_selection():
    global selected_age_gender
    selected_age_gender = request.form['selected_age_gender']
    return jsonify({'status': 'success'})

@app.route('/update_food', methods=['POST'])
def update_food():
    global selected_food
    selected_food = request.form['selected_food']
    return jsonify({'status': 'success'})

@app.route('/update_servings', methods=['POST'])
def update_servings():
    global selected_servings
    selected_servings = int(request.form['servings'])
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
