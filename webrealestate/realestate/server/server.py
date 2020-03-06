from flask import Flask, request, jsonify
import util
app = Flask(__name__)
@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        'locations':util.get_location_names()

    })
    response.headers.add('Acess-Control-Allow-Origin','*')
    return response
    

@app.route('/get_house_price', methods=['GET'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location  = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(total_sqft,location,bhk,bath)
    })
    response.header.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting python server .....")
    app.run()

