from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

# ROUTES

@app.route('/')
def index():
   return render_template('about.html')

@app.route('/myprojects')
def myprojects():
    return render_template('myprojects.html')

@app.route('/contacts', methods = ['GET', 'POST'])
def contacts():
    if request.method == 'GET':
        return render_template('contacts.html')
    elif request.method == 'POST':
        subject = request.form.get('contact-subject')
        body = request.form.get('contact-body')
        return 'Subject: {} <br> Body: {}'.format(subject, body)


# FUNCTIONS



if __name__ == '__main__':
    app.run(debug=True)

