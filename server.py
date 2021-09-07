from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key = 'shh secret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def submit():
    name = ''
    location = ''
    language = ''
    comments = ''
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        language = request.form.get('language')
        comments = request.form.get('comments')
    return render_template('submit.html', name=name, location=location,language=language, comments=comments)

if __name__=="__main__":
    app.run(debug=True)