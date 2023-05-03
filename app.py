from flask import Flask, request,jsonify

app = Flask(__name__)



from IoT_weather_station_neural_network import run_ml_model
import numpy as np
@app.route('/submit', methods=['GET','POST'])
def submit():
    wd = float(request.form['wd'])
    av_ws = float(request.form['av_ws'])
    mx_ws = float(request.form['mx_ws'])
    tem = float(request.form['tem'])
    hum = float(request.form['hum'])
    b_pr = float(request.form['b_pr'])
    wd_rad = wd*np.pi/180
    inputs = [av_ws*np.cos(wd_rad),av_ws*np.sin(wd_rad),mx_ws*np.cos(wd_rad),mx_ws*np.sin(wd_rad),tem/25 , hum /70 , b_pr/1013]
    return jsonify(run_ml_model(np.array([inputs])))
if __name__ == '__main__':
    app.run()
