from flask import Flask, render_template

app = Flask(__name__)

# homepage function
doNotStyle = ['about']


@app.route("/")
@app.route("/homepage")
def homepage():
    # return "sometxt"
    return render_template("homepage.html",
                           pageTitle="homepage",
                           pageNum=1,
                           pageName="homepage",
                           nostyle=doNotStyle,
                           nums=range(20))


@app.route("/aboutus")
def about_us():

    return render_template("aboutus.html", pageTitle="about us", pageNum=2, pageName="about", nostyle=doNotStyle)


@app.route("/add")
def add():

    return render_template("add.html", pageTitle="add", pageNum=3, pageName="add", nostyle=doNotStyle)


if __name__ == "__main__":
    app.run(debug=True)
