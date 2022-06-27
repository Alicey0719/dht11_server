from asyncore import loop
from flask import Flask, make_response, jsonify
from dotenv import load_dotenv
import RPi.GPIO as GPIO
import dht11
import os
import time
import datetime

load_dotenv()

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

PIN = int(os.getenv('PIN'))
print("using PIN is ",PIN)
sensor = dht11.DHT11(pin=PIN)

app = Flask("dht11-server")


@app.route("/")
def responce_temp():
    #初期化
    temp = 0.0
    hum = 0.0
    s_data = sensor.read()
    loop_count = 0

    # 値の取得
    while True:
        if s_data.is_valid():
            temp = round(s_data.temperature, 2)
            hum = round(s_data.humidity, 2)
            return jsonify({'temp': str(temp), 'hum': str(hum)}), 200
        else:
            loop_count += 1
            time.sleep(0.05)
            s_data = sensor.read()
            if loop_count > 100:                
                return jsonify({'error': 'Could not retrieve sensor data.'}), 500
            continue


def main():
    app.run(host='0.0.0.0', port=32121, threaded=False)

if __name__ == '__main__':
    main()