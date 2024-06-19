from flask import Flask, jsonify, render_template
import github_parser
import json
app = Flask(__name__)

@app.route('/')

def dynamic_page(): 
    thing = []
    
    prs = github_parser.get_github_pr()
    count = len(prs)
    for i in range(0,count):    
        thing.append(prs[i])
    return render_template("test.html", to_send=prs)


if __name__ == '__main__':
    app.run(host='0.0.0.0')