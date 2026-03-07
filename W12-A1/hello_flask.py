from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_flask():
    image =''
    if request.method == "POST":
        file = request.files["image"]
        file.save("static/" + file.filename)
        image = f"<h2>Uploaded Image</h2><img src='/static/{file.filename}' width='300'>"

    return f"""
        <body style='background:green; color:white'>
            <p>Hello Flask Framework!</p>
            <p> Please go to <a href='/admin'>Admin</a></p>
            <h2>Upload Image</h2>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="image">
                <input type="submit">
            </form>
            {image}
        </body>
        """


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