from flask import Flask   #from the flask module import the Flask class

app = Flask(__name__)  #create an instance of Flask into app (now an object)

@app.get("/")     #we have access to an object's methods (also a decorator)
def main():        #A wrapped function is called a view function in flask.
    me ={
        "first_name" : "Felix",
        "last_name": "Almonte",
        "hobbies" : "Drawing",
        "is_active" : True
    }

    return me       #when we return a python dictionary from a view function, 
                    #flask will automatically convert it to JSON