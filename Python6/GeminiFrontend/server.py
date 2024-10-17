from flask import Flask, render_template, request


api = Flask("__name__")

    

@api.route('/', methods = ['GET'])
def index():
    return render_template('sendfile.html')

# @api.route('/regok', methods = ['GET'])
# def index():
#     return render_template('reggok.html')

# @api.route('/regko', methods = ['GET'])
# def index():
#     return render_template('reggko.html')

if __name__ =='__main__':
    api.run(host = "0.0.0.0", port = 8085)
