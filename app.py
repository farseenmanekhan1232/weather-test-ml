from flask import Flask, request,jsonify

app = Flask(__name__)



from IoT_weather_station_neural_network import run_ml_model
import numpy as np
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='GET':
        return 'done'
    wd = int(request.form['wd'])
    av_ws = int(request.form['av_ws'])
    mx_ws = int(request.form['mx_ws'])
    tem = int(request.form['tem'])
    hum = int(request.form['hum'])
    b_pr = int(request.form['b_pr'])
    wd_rad = wd*np.pi/180
    input = [av_ws*np.cos(wd_rad),av_ws*np.sin(wd_rad),mx_ws*np.cos(wd_rad),mx_ws*np.sin(wd_rad),tem/25 , hum /70 , b_pr/1013]
    return jsonify(run_ml_model(np.array([input])))
if __name__ == '__main__':
    app.run()
