from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():#default route
    return 'hello!'

@app.route('/success/<name>') #'/success--/--<name>' the / can be replaced with any character -,$, ,  , . , .....
def success(name):#return a value from URL
    print(name)
    return 'Hello, '+name

@app.route('/page')#request HTML page
def pagego():
    return render_template('index.html')
@app.route('/addpage')
def index():
    return render_template("index.html", phrase="hello", times=5)

if __name__=="__main__":
    app.run(debug=True)