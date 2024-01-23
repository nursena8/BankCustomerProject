import joblib

loaded_model = joblib.load('models/gbm_model.joblib')

new_data=[600, 19, 1000.0, 1,10000,2]

new_=np.array(new_data).reshape(1,-1)

prediction=loaded_model.predict(new_)

prediction[0]