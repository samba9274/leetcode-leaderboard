from flask import Flask, request
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)
@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    return "<pre>"+"*LeetCode Leaderboard*<br /><br />```Rank```   ```Username```<br />"+"<br />".join([f"    {index+1}       {user[0]}" for index, user in enumerate(dict(sorted({x:requests.get(f'https://leetcode-stats-api.herokuapp.com/{x}').json()['ranking'] for x in request.args['users'].split(",")}.items(), key=lambda item: item[1])).items())])+"</pre>"
    
if __name__ == "__main__":
    app.run()