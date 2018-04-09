from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/welcome", methods=['POST'])
def signup():
    # look inside the request to figure out what the user typed
    username = request.form['user']
    security_key = request.form['pass']
    security_verify = request.form['verify']
    email = request.form['email']
    verifys = [username, security_key, security_verify]
    at = 0
    period = 0
    #if username is less than 3 char or more than 20 return error
    if (not username) or (username.strip() == ""):
        error = "Please enter a valid username."
        return redirect("/?error=" + error)
    if len(username) < 3 or len(username) > 20:
        error = "Invalid Username length"
        return redirect("/?error=" + error)
    #if password is less than 3 char or more than 20 return error
    if (not security_key) or (security_key.strip() == ""):
        error = "Please enter a valid password"
        return redirect("/?error=" + error)
    if len(security_key) < 3 or len(security_key) > 20:
        error = "Invalid Password length"
        return redirect("/?error=" + error)
    #if verify is less than 3 char or more than 20 return error
        #if password != verify return error
    if (not security_verify) or (security_verify.strip() == "") or (security_key != security_verify):
        error = "Please verify your passwords match."
        return redirect("/?error=" + error)
    if len(security_verify) < 3 or len(security_verify) > 20:
        error = "Invalid Password length"
        return redirect("/?error=" + error)

    for n in verifys:
        if (' ' in n):
            error = "Please ensure Username and Passwords have no spaces."
            return redirect("/?error=" + error)

    #The criteria for a valid email address in this assignment are that it 
    #has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    if email != '' and len(email) < 3 or len(email) > 20:
        error = "Invalid Email, too many characters"
        return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    username_escaped = cgi.escape(username, quote=True)
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()