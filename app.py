from flask import Flask, render_template, request


app = Flask(__name__)
  

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('index.html')

#at

# @app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact')
def contact():
    return render_template('contact.html')


# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
