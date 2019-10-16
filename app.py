from flask import Flask, render_template, url_for, request
import requests

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST', 'GET'])
def user_download():
    url = request.form['url']  # user provides url in query string
    r = requests.get(url, stream=True)
    total_length = int(r.headers.get('content-length'))
    done=0
    done_list=[]
    left_list=[]
    for data in r.iter_content():
        done += len(data)   # Keep track of file length downloaded
        done_list.append(done)
        if total_length-done<0:
            exit
        else:
            left=total_length-done  # Keep track of file length left to be downloaded
            left_list.append(left)
    return render_template('display.html', total=total_length, done=done_list, left=left_list)
    
if __name__=="__main__":
    app.run(debug=True)