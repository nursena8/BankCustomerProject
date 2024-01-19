from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Eğitilmiş modeli yükle
loaded_model = joblib.load('gbm_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        new_data = [float(request.form['credit_score']),
                    float(request.form['age']),
                    float(request.form['balance']),
                    float(request.form['products_number']),
                    float(request.form['estimated_salary']),
                    float(request.form['tenure']),
                    int(request.form['credit_score_group_Very_Poor']),
                    int(request.form['credit_score_group_Mid_Poor']),
                    int(request.form['credit_score_group_Poor']),
                    int(request.form['credit_score_group_Fair']),
                    int(request.form['credit_score_group_Good']),
                    int(request.form['credit_score_group_Excellent'])]

        new_data = np.array(new_data).reshape(1, -1)

        prediction = loaded_model.predict(new_data)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
