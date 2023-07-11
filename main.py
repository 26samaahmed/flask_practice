from flask import Flask, escape, redirect, url_for, request, render_template  # we import the Flask class
# creating an instance of the class, __name__ is used to identify the root path of the application
app = Flask(__name__) 

@app.route("/hi")  # to tell Flask what URL should trigger the function
def hello_world():
    return "<p> Hello World </p>"

@app.route("/testing")
def employer_info():
    return "Hello, I'm Sama and I am learning Flask Yahoo"

# to prevent XSS attacks, we use escape() by converting special characters in a string into their corresponding HTML entities

@app.route("/testing2")
def testing_escape():
    user_input = '<script>alert("XSS attack"); </script>' 
    escaped_input = escape(user_input) 
    return f"Escaped: {escaped_input}"

'''
When you write a function with the @app.route decorator, it tells Flask that whenever a user accesses a specific URL (the route) 
on your website, Flask should execute that Python function and return the result as the response to the user's request.
'''

# if i type in my url /sama, then this would print Hello, Sama
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/about")
def home():
    return redirect(url_for("about"))

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/post/int:<id>") # the int: is used to convert the id to an integer
def user_id(id): 
    return f"User ID: {id}" 

@app.route("/path/<path:subpath>") # the path: is used to convert the subpath to a path
def user_subpath(subpath):
    return f"Subpath: {subpath}"

@app.route("/test1")
def test1():
    return "Test1"

@app.route("/test2")
def test2():
    return "Test2"

@app.route("/user/<username>")
def user_greet(username):
    return f"Welcome Back, {username}"

with app.test_request_context():
    print(url_for('test1'))  # url_for() is used to build a URL to a specific function
    print(url_for('test2')) # it takes the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule
    print(url_for('test2', next='/')) # the next=/ is used to redirect to the home page
    print(url_for('user_greet', username='gyma')) # the username= is used to pass the username to the user_greet function

@app.route('/login', methods=['GET', 'POST']) # the methods= is used to tell Flask that this view function accepts GET and POST requests
def login():
    if request.method == "POST":
        return "Post method"
    else:
        return "Get method"

@app.route("/", methods=['GET', 'POST'])
def user_info():
    if request.method == "POST":  # if the request method is POST, then the user has submitted the form
        name = request.form.get("name") # request.form.get() is used to get the value of the name field from the form
        password = request.form.get("password") # request.form.get() is used to get the value of the password field from the form
        return f"Hello, {name} and your password is {password}. MISSION COMPLETE YAHOO"
    else:
        return render_template("index.html") # render_template() is used to render a template, which is a file that contains static data as well as placeholders for dynamic data
    # the render_template() function takes the name of the HTML file as its first argument and any number of keyword arguments, each corresponding to a variable that you want to pass to the HTML file

@app.get("/getandpost")
def get():
    return render_template("index.html")

@app.post("/getandpost")
def post():
    return "MISSION REACHED"

if __name__ == '__main__':
    app.run(debug=True)
    # debug=True is used to run the application in debug mode, which will reload the server each time you make a change in the code

# a GET method is used to request data from a specified resource like displaying a webpage or a form to a user
# a POST method is used to send data to a server to create/update a resource for storing in a database