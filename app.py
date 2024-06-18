from flask import Flask, jsonify, render_template
import github_parser
import json
app = Flask(__name__)

@app.route('/')

def dynamic_page(): 
    thing = []
    
    stuff = github_parser.get_github_pr()
    count = len(stuff)
    for i in range(0,count):    
        thing.append(stuff[i])
    return render_template("test.html", to_send=stuff)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)