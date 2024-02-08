from flask import Flask 
app = Flask(__name__) #creating an object
#created application now creating a route
@app.route("/") #when url / is accessed then run hello world
def hello_world():
  return "Hello World"
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  