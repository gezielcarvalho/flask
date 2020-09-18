from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
from flask import make_response
from flask import render_template

app = Flask(__name__)

@app.route('/redirected', methods=['GET'])
def redirected():
    return 'Redirecionado',200

@app.route('/<name>/<int:age>', methods=['POST'])
def nome(name,age):
    return 'Hello, %s! My age is %d' % (name,age),200

@app.route('/request', methods=['POST'])
def request_data():
    # person = request.args.get('person')
    person = request.form['person']
    age = request.form['age']
    resultado = "Hello! My name is %s and I'm %s years old!" %(person, age)
    return resultado

# @app.route('/response', methods=['POST'])
# def response_data():
#     obj = {
#         'username':'Zeh',
#         'facebook':'https://facebook.com/geziel.carvalho',
#         'github'  :'https://github.com/gezielcarvalho'
#     }
#     return jsonify(obj)

# @app.route('/response', methods=['GET'])
# def response_data():
#     return redirect(url_for('redirected'))

@app.route('/response', methods=['POST'])
def response_data():
    obj = {
        'username':'Zeh',
        'facebook':'https://facebook.com/geziel.carvalho',
        'github'  :'https://github.com/gezielcarvalho'
    }
    resp = make_response(jsonify({'data':request.form,'obj':obj}), 201)
    resp.headers['Course Powered By'] = 'Sabre Software'
    return resp

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:
        return redirect(url_for('result', nome = request.form['nome']))

@app.route('/result/<nome>',methods=['GET'])
def result(nome):
    return render_template('index.html', nome = nome)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error),404


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8004, debug=True)