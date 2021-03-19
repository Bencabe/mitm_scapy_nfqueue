from flask import Flask, render_template,jsonify,request
import json




# EB looks for an 'application' callable by default.
app = application = Flask(__name__)



@application.route("/")
def index():
    return render_template('index.html')


@application.route("/display_text")
def display_text():
    input = request.args.get('input')
    return jsonify(res=input)



# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
