from flask import Flask, render_template, redirect, request
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
# @app.route('/works.html')
# def works():
#     return render_template('works.html')   

# @app.route('/about.html')
# def about():
#     return render_template('about.html')  

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong, please try again"

def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = db.write(f'\n {email}, {subject}, {message}')        
    
