from flask import Flask, render_template, request

my_app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def root():
    print request.header;
    print request.method;
    print request.args;
    print request.form;
    return render_template('form.html')

@app.route("/response", methods = ['GET','POST'])
def response():
    return render_template("response.html", username = request.form["data"], method = request.method)

if __name__ == '__main__':
    my_app.debug = True;
    my_app.run()

