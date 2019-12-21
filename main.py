from flask import Flask, render_template, request
import re
 
app = Flask(__name__)
 
 
def search_player(text):


    player_list = ['EliGE','Stewie2k','NAF','nitr0','Twistzz']

    player_list_hit = [s for s in player_list if text in s]

    return player_list_hit
 
 
@app.route('/', methods=['POST', 'GET'])
def home():
 
    search_result = ''
 
    if request.method == 'POST':
        text = request.form['text']
        search_result = search_player(text)
 
        return render_template('main.html', result=search_result, sentence=text)
 
    return render_template('main.html', result=search_result)
 
 
if __name__ == "__main__":
    app.run(debug=True)