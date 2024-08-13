import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
from pydantic import BaseModel
import pandas as pd
# 2. Create the app object
from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware to allow requests from all origins
class BankCredit(BaseModel):
    distance_from_home: float
    distance_from_last_transaction: float
    ratio_to_median_purchase_price: float
    repeat_retailer: float
    used_chip: float
    used_pin_number: float
    online_order: float
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
pickle_in = open("Credit.pickle4","rb")
classifier=pickle.load(pickle_in)
def transf():
    return classifier

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict(data: BankCredit):
    distance_from_home = data.distance_from_home
    distance_from_last_transaction = data.distance_from_last_transaction
    ratio_to_median_purchase_price = data.ratio_to_median_purchase_price
    repeat_retailer = data.repeat_retailer
    used_chip = data.used_chip
    used_pin_number = data.used_pin_number
    online_order = data.online_order
    prediction = classifier.predict([[distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order]])
    if(prediction[0]==1):
        prediction="Fake Card"
    else:
        prediction="Legit"
    return {
        'prediction': prediction
    }
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')