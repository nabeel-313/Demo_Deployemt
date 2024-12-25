"""
This module contains test cases for the Flask application in app.py.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/homepage', methods=['GET', 'POST']) # To render Homepage
def home_page():
    '''
    This function will render homepage
    this will help to know about homepage
    Hope it will work fine now
    '''
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    '''
    This function will render Result page
    now this deployment on k8s
    '''
    if request.method=='POST':
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation=='add':
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'the result when ' + str(num1) + ' isdividedby ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
