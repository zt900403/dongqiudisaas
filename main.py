from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from flask import render_template
from api import dongqiudi


app = Flask(__name__,
            static_folder="./static",
            template_folder="./static",
            static_url_path='/')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/getallleagues')
def getallleagues ():
    data = dongqiudi.get_all_leagues()
    return jsonify(data)

@app.route('/api/getallmatches')
def getallmatches ():
    url = request.args.get('url', '')
    data = dongqiudi.get_all_matches(url)
    for one in data:
        one['beijingTime'] = dongqiudi.utcstr2localstr(one['start_play'])
    return jsonify(data)

@app.route('/api/getexceltemplate')
def getexceltemplate ():
    url = request.args.get('url', '')
    data = dongqiudi.get_all_matches(url)

    matchid = request.args.get('matchid', '')

    if not url and not matchid:
        return {
            'status': 'error',
            'msg': 'no input'
        }

    match = dongqiudi.getProperty(data, 'match_id', matchid)

    teamAid = match['team_A_id']
    teamBid = match['team_B_id']
    
    teamAinfo = dongqiudi.get_team_info(teamAid)
    teamBinfo = dongqiudi.get_team_info(teamBid)
    contrast = dongqiudi.get_pre_analyze_data_contrast(match['match_id'])
    teamAmainPerson = dongqiudi.get_main_person(teamAid)
    teamBmainPerson = dongqiudi.get_main_person(teamBid)

    filename = dongqiudi.writeToExcel(match, teamAinfo, teamAmainPerson, teamBinfo, teamBmainPerson, contrast)
    response = make_response(app.send_static_file(filename))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response