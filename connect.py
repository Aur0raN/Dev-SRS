from flask import request, Flask
from flask_cors import CORS
from CoreFunction import *
import base64
# Flask API used to connect to frontend
app=Flask(__name__)
CORS(app)
@app.route("/test", methods=["POST"])
def getData():
    #variable used for image file path
    imgAddress = 'D:\\images\\image2.jpeg'

    data=request.get_json()
    print(data)
    rawImgString = data["address"]
    imgString = rawImgString[23:]
    image_64_decode = base64.b64decode(imgString)
    image_result = open(imgAddress, 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)

    

    #Calling image preprocessing functions
    removeWhiteSpace(imgAddress, imgAddress)
    DetectAngle(imgAddress)
    removeWhiteSpace(imgAddress, imgAddress)
    thinArray(imgAddress)

    percentage = compare(readBlobImg(data["custId"]), imgAddress)
    print(percentage)
    return percentage

if __name__ == '__main__':
    app.run()