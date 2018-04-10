from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/welcome", methods=['POST'])
def signup():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    security_key = request.form['pass']
    security_verify = request.form['verify']
    email = request.form['email']
    at = 0
    period = 0
    keyerror =""
    erroruser=""
    verifyerror =""
    emailerror =""
    if (not username) or (username.strip() == ""):
        erroruser = "Please enter a valid username."
    if len(username) < 3 or len(username) > 20:
        erroruser = "Invalid Username length"
    if (not security_key) or (security_key.strip() == ""):
        keyerror = "Please enter a valid password"
    if len(security_key) < 3 or len(security_key) > 20:
        keyerror = "Invalid Password length"
    if (not security_verify) or (security_verify.strip() == "") or (security_key != security_verify):
        verifyerror = "Please verify your passwords match."
    if len(security_verify) < 3 or len(security_verify) > 20:
        verifyerror = "Invalid Password length"
    if (' ' in username):
        erroruser = "Please ensure Username has no spaces."
    for n in email:
        if n == "@":
            at = at +1
            if at > 1:
                emailerror = "Please ensure email only has one @"
        if n == ".":
            period = period + 1
            if period > 1:
                emailerror = "Please ensure email only has one ."
    if email != '' and len(email) < 3 or len(email) > 20:
        emailerror = "Invalid Email, too many characters"
    if erroruser != "" or keyerror != "" or verifyerror != "" or emailerror != "":
        return render_template('signup.html', erroruser=erroruser, keyerror=keyerror, verifyerror=verifyerror, emailerror=emailerror)
    else:
        return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('signup.html')

app.run()