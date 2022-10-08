from flask import Flask,render_template,request
from main import main
 
app = Flask(__name__)


@app.route('/')
def hi():
    return main('china')
 
@app.route('/tweet/<topic>')
def generator(topic):
    return main(topic)

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        topic = form_data['Topic']
        username = form_data['User']
        print(username)
        tweet = main(topic, username)
        format = '@' + username + '- ' + tweet
        return render_template('form.html') + format

 
 

if __name__ == "__main__":
    app.run(debug=True)