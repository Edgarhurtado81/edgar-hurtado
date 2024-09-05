from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/enviado', methods=['POST'])
def enviado():
    if request.method == 'POST':
        nom = str(request.form['nombre'])
        tel = int(request.form['telefono'])
        ema = str(request.form['email'])
        mens = str(request.form['tema'])
        return render_template('enviado.html', nombre=nom, telefono=tel, email=ema, mensaje=mens)


if __name__ == '__main__':
    app.run(port=5030)