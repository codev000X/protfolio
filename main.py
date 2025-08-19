from flask import Flask, render_template,request , redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("project.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # handle form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return redirect('/thank-you')  # or flash a message
    return render_template('contact.html')



@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == "__main__":
    app.run()



