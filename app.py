from flask import Flask 
#To use templates we have to use render remplates
from flask import render_template, jsonify
app = Flask(__name__) #creating an object
#database to directly change rather than modify html
Jobs=[
  {
    'id':1,
    'Title': 'Data Scientist',
    'Location':'Hyderabad',
    'Salary': 'Rs 100000'
    
  },
  {
    'id':2,
    'Title': 'Data Analyst',
    'Location':'Hyderabad',
    'Salary': 'Rs 100000'

  },
  {
    'id':3,
    'Title': 'Data Intern',
    'Location':'Hyderabad',
    'Salary': 'Rs 10000'

  },
  {
    'id':4,
    'Title': 'Backend engineer',
    'Location':'Hyderabad',
    'Salary': 'Rs 90000'

  }
]
#created application now creating a route
@app.route("/") #when url / is accessed then run hello world
def hello_world():
  return render_template('home.html', jobs=Jobs, Student_name='Anees')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  