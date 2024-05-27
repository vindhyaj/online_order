import json

from flask import Flask, request, Response
import order

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/orders', methods=['POST'])
# ‘/’ URL is bound with hello_world() function.
def place_order():
    try:
        order.ParseOrder(request.get_json())
        return Response("OK", status=200, mimetype='application/json')
    except Exception as e:
        print(f"Exception {e}")
        return Response(f"Error. {e}", status=500, mimetype='application/json')

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
