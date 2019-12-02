from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

acts=[
    {"id":1,"name":"joe","totalVotes":4},
    {"id":2,"name":"joe2","totalVotes":5},
]

nextId=3
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello World"

@app.route('/acts')
def getAll():
    return jsonify(acts)

@app.route('/acts/<int:id>')
def findById(id):
    foundActs = list(filter(lambda t: t['id'] == id, acts))
    if len(foundActs) == 0:
        return jsonify({}), 204
    return jsonify(foundActs[0])

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\", \"Author\":\"Someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/acts', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    #put some other checks here
    act = {
        "id": nextId,
        "name": request.json['name'],
        "totalVotes":0,
    }
    nextId += 1
    acts.append(act)
    return jsonify(act)


@app.route('/acts/<int:id>', methods=['DELETE'])
def delete(id):
    foundActs = list(filter(lambda t: t['id'] == id, acts))
    if (len(foundActs) ==0):
        abort(404)
    acts.remove(foundActs[0])
    return jsonify({"Done":True})

@app.route('/votes/<int:actId>', methods = ['POST'])
def addVote(actId):
    foundActs = list(filter(lambda t:t['id']== actId, acts))
    if len(foundActs)==0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'votes' in request.json or type(request.json['votes']) is not int:
        abort(401)
    newVotes = request.json['votes']
    foundActs[0]['totalVotes'] += newVotes
    return jsonify(foundActs[0])

@app.route('/votes/leaderobard')
def getleaderboard():
    acts.sort(key = lambda x: x['totalVotes'], reverse = True)
    return jsonify(acts)

if __name__ == '__main__':
    app.run(debug= True)