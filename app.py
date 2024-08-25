from flask import Flask, render_template, request, send_file, Response
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    qr = qrcode.make(data)
    buf = io.BytesIO()
    qr.save(buf)
    buf.seek(0)
    return send_file(buf, mimetype='image/png', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
