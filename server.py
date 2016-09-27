from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)
import serial
ser = serial.Serial("/dev/ttyACM0", 9600)
@app.route('/', methods = ['POST','GET'])
def home():
    author = "lemonS"
    text = request.form['text']
    ser.write(text.encode('ascii'))
    if request.method == 'POST':
        if request.form['submit'] == 'Ligar':
            ser.write('a')
        elif request.form['submit'] == 'Desligar': 
            ser.write('A')
        elif request.form['submit'] == 'Ligar2':
            ser.write('b')
        elif request.form['submit'] == 'Desligar2':
            ser.write('B')
        else:
            pass
    return render_template('index.html', author=author)
if __name__ == "__main__":
    app.run(host='192.168.1.8', port=8080, debug = True)