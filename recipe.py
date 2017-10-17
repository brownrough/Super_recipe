from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def showHome():
    return render_template('index.html')

@app.route('/signUp')
def signUp():
    return render_template('signup.html')

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/<name>')
def redirectHome(name):
    if name == 'index':
        return redirect(url_for('homepage'))

@app.route('/category')
def category():
    return render_template('categories.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)