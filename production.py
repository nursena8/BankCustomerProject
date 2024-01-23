import joblib
loaded_model = joblib.load('gbm_model_production.joblib')
new_data=[600, 19, 1000.0, 1,10000,2]

new_=np.array(new_data).reshape(1,-1)
prediction_gbm_model=loaded_model.predict(new_)
prediction_gbm_model[0]