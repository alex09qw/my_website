from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Kiev, Ukraine',
    'salary': 'GRN 70,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Lviv, Ukraine',
    'salary': 'GRN 85,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Washington D.C., USA',
    'salary': '$ 150,000'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs=JOBS,
                          company_name='MyComp')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)