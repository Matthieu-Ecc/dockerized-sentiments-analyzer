from flask import Flask , request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        sentence = request.args.get("data")
        f  = open("logs.txt","w")
        f.write(sentence)
        f.close
        return {'sentence': sentence}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)