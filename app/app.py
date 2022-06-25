from flask import Flask, make_response, request
#import RPi.GPIO as GPIO
#import dht11
import time
import datetime

app = Flask("dht11-server")

@app.route("/")
def responce_temp():
    res = make_response()
    
    #データ作る
    res.data = 'test'

    res.mimetype = 'application/json' 
    return res


def main():
    app.run(host='0.0.0.0', port=32121, threaded=False)

if __name__ == '__main__':
    main()