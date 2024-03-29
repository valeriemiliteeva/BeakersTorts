# import requests
from flask import Flask, render_template, request

from quiz import quiz_data

from query import query_colleges

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/easteregg/')
def easteregg():
    return render_template("easteregg.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html",
                           data=quiz_data(),
                           question_index=0,
                           answers='{}')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/colleges')
def colleges():
    return render_template("colleges.html")


@app.route('/billy')
def about_billy():
    return render_template("aboutbilly.html")


@app.route('/lola')
def about_lola():
    return render_template("aboutlola.html")


@app.route('/michael')
def about_michael():
    return render_template("aboutmichael.html")


@app.route('/valerie')
def about_valerie():
    return render_template("aboutvalerie.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/responses/')
def responses():
    return render_template("responses.html")


@app.route('/next', methods=['POST'])
def next_question():
  print(request.form['answer'])
  print(request.form['answers'])
  print(request.form['next_question'])
  return render_template("quiz.html",
                         data=quiz_data(),
                         question_index=int(request.form['next_question']),
                         answers=request.form['answers'])


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form['answers'])
    colleges = query_colleges(request.form['answers'])
    return render_template("results.html", colleges=colleges)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='3000')
