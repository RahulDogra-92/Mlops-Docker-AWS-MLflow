import pytest
from app import app # just trying to access the flask app
import json

@pytest.fixture        
def client():                      # will reuse this server for all endpoints
    return app.test_client() 

def test_ping(client):                # test for '/ping' API
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message" : "hey"}


def test_predict(client):
    test_data =  {
        "Gender" : "Male",
        "ApplicantIncome" : 50000,
        "LoanAmount" : 500000
    }
    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status': "Approved"}

