from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page='profil')

@app.route('/geschichte')
def geschichte():
    return render_template('index.html', page='geschichte')

@app.route('/unsere-produkte')
def unsere_produkte():
    return render_template('index.html', page='produkte')

@app.route('/ziele')
def ziele():
    return render_template('index.html', page='ziele')

@app.route('/unsere-partners')
def unsere_partners():
    return render_template('index.html', page='partners')

if __name__ == '__main__':
    app.run(debug=True)
