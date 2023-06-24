from flask import Flask, request   #from the flask module import the Flask class

app = Flask(__name__)  #create an instance of Flask into app (now an object)
USERS =[]

@app.get("/users/<int:user_id>")
@app.get("/<int:user_id>")     #we have access to an object's methods (also a decorator)
def main(user_id):
    me = {}    
    not_found = True
    if user_id==1:   
        not_found=False #A wrapped function is called a view function in flask.
        me ={
        "first_name" : "Felix",
        "last_name": "Almonte",
        "hobbies" : "Drawing",
        "is_active" : True
        }
    if not_found:
        return me, 404
    
    return me #flask default is 200
           #when we return a python dictionary from a view function, 
                    #flask will automatically convert it to JSON

@app.get("/users/")
def get_users():
    return USERS

@app.post("/users/")
def create_user():
    raw_data = request.json
    USERS.append(raw_data)
    return 201, {"message": "created"}


    # REST 
    # is an architectural guide for building network connected APIs
    # Representational State Transfer
    # Endpoints are named after the resource they manage, but in plural like:
    # /users, /pets, /products.
    # Most APIs help support CRUD (create, read, update, delete, (scan)) operations
    # create - > POST
    # read -> GET a single resource
    # UPDATE -> PUT/PATCH 
    # DELETE -> Delete
    # (SCAN )-> GET (get an entire collection of records, like an entire database)