from flask import Flask, escape, redirect, url_for  # we import the Flask class
# creating an instance of the class, __name__ is used to identify the root path of the application
app = Flask(__name__)


@app.route("/")  # to tell Flask what URL should trigger the function
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


@app.route("/user/<username>")
def user_greet(username):
    return f"Welcome Back, {username}"


if __name__ == '__main__':
    app.run(debug=True)
    # debug=True is used to run the application in debug mode, which will reload the server each time you make a change in the code
