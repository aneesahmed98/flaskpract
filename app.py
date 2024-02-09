from flask import Flask 
#To use templates we have to use render remplates
from flask import render_template
app = Flask(__name__) #creating an object
#created application now creating a route
@app.route("/") #when url / is accessed then run hello world
def hello_world():
  return render_template('home.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  