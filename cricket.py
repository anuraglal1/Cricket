from pycricbuzz import Cricbuzz
import json
from flask import Flask, render_template, request
import requests

app=Flask(__name__) 

@app.route('/score',methods=['POST'])
def score():
        c=Cricbuzz()
        matches=c.matches()
        post_id1=request.form.get('live score')
        post_id2=request.form.get('commentary')
        post_id3=request.form.get('scorecard')
        if post_id1 is not None:
                #print(matches)
                x=[]
                cnt=0
                for match in matches:
                        x.append(json.dumps(c.livescore(match['id']),indent=4))
                        cnt+=1
                q=1
                return render_template('score.html',y=x,count=cnt,id=q)
        if post_id2 is not None:
                x=[]
                cnt=0
                for match in matches:
                        x.append(json.dumps(c.commentary(match['id']),indent=4))
                        cnt+=1
                q=2
                return render_template('score.html',y=x,count=cnt,id=q)
        if post_id3 is not None:
                x=[]
                cnt=0
                for match in matches:
                         x.append(json.dumps(c.livescore(match['id']),indent=4))
                         cnt+=1
                q=3
                return render_template('score.html',y=x,count=cnt,id=3)
        return None
                        
                

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

