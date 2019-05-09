from flask import Flask, request, Response, send_file
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def GreyScale():
    '''r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''
    img = cv2.imread("naturo-monkey-selfie.jpg",1);
    img_str = cv2.imencode('.jpg', img)[1].tostring()
    # build a response dict to send back to client
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
	
    


# start flask app
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
