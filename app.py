import pickle
from flask import Flask, request, Response, jsonify

# loading the model 
model_pickle = open("./artefacts/classifier.pkl", 'rb')
clf = pickle.load(model_pickle)

app = Flask(__name__)

# defining the function for the /ping endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return {"message" : "hey"}

@app.route('/params', methods=['GET'])
def get_app_param():
    parameters =  {
        "Gender" : "<Male/Femal>",
        "ApplicantIncome" : "<ApplicantIncome>",
        "LoanAmount" : "<LoanAmount>"
    }
    return parameters

# defining the function for the /predict endpoint
@app.route('/predict', methods=['POST'])
def prediction():
    # Pre-processing user input
    loan_req = request.get_json()
    print(loan_req) 

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] 

    # Making predictions
    prediction = clf.predict([[Gender, ApplicantIncome, LoanAmount,]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    return {'loan_approval_status': pred}

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)
