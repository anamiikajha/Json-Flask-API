from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This our / api endpoint!'

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'message':input_json['message']}
     return jsonify(dictToReturn)
# blog posts api endpoint
@app.route('/posts/')
def blog():
    return jsonify({'title':'How to learn Go',
    'content':'How to learn Go lang in 2022',
    'author':'Anamika'},
    {'title':'How to learn Angular',
        'content':'How to learn Angular with node js and using apis to contact to the backend like Django, Flask or Node js',
        'author':'Anamika'})
