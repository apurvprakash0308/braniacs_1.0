from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')	

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/analyst")
def analyst():
	return render_template('analyst.html')

@app.route("/contactus")
def contactus():
	return render_template('contactus.html')

@app.route("/faqs")
def faqs():
	return render_template('faqs.html')

@app.route("/mcq1")
def mcq1():
	return render_template('mcq1.html')

@app.route("/mcq2")
def mcq2():
	return render_template('mcq2.html')

@app.route("/mcq3")
def mcq3():
	return render_template('mcq3.html')

@app.route("/mcq4")
def mcq4():
	return render_template('mcq4.html')

@app.route("/ourservices")
def ourservices():
	return render_template('ourservices.html')

@app.route("/personality")
def personality():
	return render_template('personality.html')

@app.route("/result")
def result():
	return render_template('result.html')

@app.route("/resultp")
def resultp():
	return render_template('resultp.html')

@app.route("/reviews")
def reviews():
	return render_template('reviews.html')

@app.route("/signup")
def signup():
	return render_template('signup.html')

@app.route("/test1")
def test1():
	return render_template('test1.html')

@app.route("/test2")
def test2():
	return render_template('test2.html')

@app.route("/test3")
def test3():
	return render_template('test3.html')

if __name__ == '__main__':
	app.run(debug=True)