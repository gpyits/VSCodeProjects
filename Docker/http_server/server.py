from flask import Flask, render_template

api=Flask('__name__')

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

api.run(host='0.0.0.0', port=8088)