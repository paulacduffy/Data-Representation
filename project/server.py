from flask import Flask, jsonify, request, abort
from stockDAO import stockDAO
from flask_cors import CORS
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app,resources={r"/*": {"origins": "*"}})

#curl "http://127.0.0.1:5000/books"
@app.route('/stock')
def getAll():
    #print("in getall")
    results = stockDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/stock/<int:id>')
def findById(id):
    foundStock = stockDAO.findByID(id)

    return jsonify(foundStock)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/stock', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    stock = {
        "itemtype": request.json['itemtype'],
        "label": request.json['label'],
        "price": request.json['price'],
    }
    values =(stock['itemtype'],stock['label'],stock['price'])
    newId = stockDAO.create(values)
    stock['id'] = newId
    return jsonify(stock)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/stock/<int:id>', methods=['PUT'])
def update(id):
    foundStock = stockDAO.findByID(id)
    if not foundStock:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'itemtype' in reqJson:
        foundStock['itemtype'] = reqJson['itemtype']
    if 'label' in reqJson:
        foundStock['label'] = reqJson['label']
    if 'price' in reqJson:
        foundStock['price'] = reqJson['price']
    values = (foundStock['itemtype'],foundStock['label'],foundStock['price'],foundStock['id'])
    stockDAO.update(values)
    return jsonify(foundStock)
        

    

@app.route('/stock/<int:id>' , methods=['DELETE'])
def delete(id):
    stockDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)