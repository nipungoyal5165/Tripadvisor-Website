# Import necessary libraries and modules
from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3 as sql

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for displaying search results
@app.route('/searchresults', methods=['POST', 'GET'])
def search_results():
    return render_template('searchresults.html')

# Define a route for prompting users to log in
@app.route('/usermustlogin', methods=['POST', 'GET'])
def usermustlogin():
    return render_template('signin.html')

# Define a route for the review submission page
@app.route('/reviewsubmission', methods=['POST', 'GET'])
def reviewsubmission():
    return render_template('reviewsthankyou.html')

# Define a route for an about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define a route for the user's shopping cart
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Define a route for a contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Define a route for displaying reviews
@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

# Define a route for user settings
@app.route('/settings')
def settings():
    return render_template('settings.html')

# Define a route for user sign-in
@app.route('/signin')
def signin():
    return render_template('signin.html')

# Define a route for handling user sign-in and authentication
    # this is the login functionality
    # current design of the login system
    # if authentication is successful, the user is redirected to the home page
    # if not, the user gets an error message and can try again.
@app.route('/usersignin', methods=['POST', 'GET'])
def user_signin():
    # This is the login functionality
    if request.method == "POST":
        msg = None
        emailaddressofuser = request.form['email']
        passwordofuser = request.form['password']
        con = sql.connect("travellogin.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from Users where Email=? and Password=?", (emailaddressofuser, passwordofuser))
        rows = cur.fetchone()
        if rows:
            con.close()
            return render_template('booking made.html')
        else:
            con.close()
            msg = "Wrong email address and/or password!"
            return render_template('signin.html', msg=msg)

# Define a route for user registration
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Define a route for registering a new user
@app.route('/registertheuser', methods=['POST', 'GET'])
def registertheuser():
    # Code to insert a new user record into the travel login database
    if request.method == 'POST':
        emailaddressofuser = request.form['email']
        passwordofuser = request.form['password']
        confirmpasswordofuser = request.form['confirmpassword']
        if not emailaddressofuser or passwordofuser:
            # Check if the password fields match
            if confirmpasswordofuser != passwordofuser:
                msg = "Passwords do not match!"
                return render_template('registration.html', msg=msg)
            else:
                with sql.connect("travellogin.db") as con:
                    cur = con.cursor()
                    cur.execute("insert into Users(Email, Password) values (?,?)", (emailaddressofuser, passwordofuser))
                    con.commit()
                    msg = "New user successfully added"
        else:
            msg = "New user: error in insert operation"
            con.rollback()
            return render_template('registration.html', msg=msg)
    
    # Redirect the user back to the homepage once registration is successful
    return render_template('index.html', msg=msg)

# Run the Flask app if this script is the main entry point
if __name__ == '__main__':
    app.run(debug=True)