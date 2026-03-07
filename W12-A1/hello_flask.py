from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello Flask Framework!</p> <p> Please go to <a href='/admin'>Admin</a></p>"

@app.route("/admin")
def admin():
    return "<p>Hello Admin!</p><img src='/static/logo.png'>"

@app.route("/bye")
def bye():
    return "<p>Bye Flask!</p>"

@app.route("/username/<name>/<user_id>")
def username(name, user_id):
    return f"Hello {name.capitalize()} : {user_id}"





if __name__ == "__main__":
    app.run(debug=True)