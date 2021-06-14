from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'I have a secret'

@app.route('/')
def main():
    if not "visit" in session:
        session["visit"] = 0
    session["visit"] += 1
    return render_template('index.html', times = session["visit"])

@app.route('/destroy', methods=['POST', 'GET'])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/increment_counter', methods=['POST'])
def increment():
    print(request.form)
    print('in increment()')
    session['visit'] += 1

    print('redirecting to /')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)