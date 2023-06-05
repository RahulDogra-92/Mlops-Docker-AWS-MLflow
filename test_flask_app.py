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

    # So your testing part is done and if testing part is done what did we actually completed in CI/CD section?
    # ANS- The CI part, we have integrated the code, so this is integration and what if I change my code then other things would break?  

