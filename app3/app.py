from flask import Flask, request, Response
from functools import wraps

app = Flask(__name__)

def auth(fn):
    wraps(fn)
    def decorated(*args, **wargs):
        auth = request.authorization
        if not auth or not (auth.username == 'admin' and auth.password == 'admin') :
            return Response('Não autorizado!', 401, { 'WWW-Authenticate': 'Basic realm="Login required"' } )
        return fn(*args, **wargs)
    return decorated

@app.route('/')
@auth
def secret_router():
    return "Rota autenticada"

if __name__ == '__main__':
    app.run(port=5003,debug=True)
