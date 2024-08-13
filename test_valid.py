from main import transf
import numpy as np
def test_predict():
    classifier=transf()
        
    x=[[0.421681,-0.177478,-0.015702,1.0,1.0,0.0,0.0]]

    prediction = classifier.predict(x)
    assert isinstance(prediction[0], np.float64)