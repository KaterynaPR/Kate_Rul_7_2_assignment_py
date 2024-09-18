from flask import Flask
app = Flask(__name__) #Create a Flask application
@app.route('/') #Implement a Flask route
def home():
    return "Hello, Flask!"
#if __name__ == '__main__':
   # app.run(debug=True)

from flask import jsonify
app = Flask(__name__) #Create a Flask application
request_counter = 0 #Global variable for counting the number of requests

@app.route('/count-requests', methods=['GET']) #Route for counting requests
def count_requests():
    global request_counter #accessing a global variable
    request_counter += 1  #increase the counter with each request
    return jsonify({'request_count': request_counter})  #return the counter in JSON format

#if __name__ == '__main__':
    #app.run(debug=True)

from flask import request
app = Flask(__name__) #Create a Flask application
request_counter = 0 #Global variable for counting the number of requests

@app.route('/count-requests', methods=['GET']) #Route for counting requests
def count_requests():
    global request_counter #accessing a global variable
    request_counter += 1 #increase the counter with each request
    return jsonify({'request_count': request_counter}) #return the counter in JSON format

@app.route('/reset-counter', methods=['POST']) #route to reset the counter
def reset_requests():
    global request_counter
    request_counter = 0  #Reset the counter to 0
    return jsonify({'message': 'Request counter has been reset', 'request_count': request_counter})

if __name__ == '__main__':
    app.run(debug=True)

