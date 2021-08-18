from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/belajar-flask')
def belajar_flask():
    return "aku sedang belajar flask!"