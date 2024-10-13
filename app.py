from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

SyntaxBank = {
    "operators": ["+", "-", "*", "/", "="],
    "keywords" : ["for","while","if", "else","elif", "in"],
    "litfun" : ["int", "print", "float", "range", "len", "string", "bool","dict",
                "str","list","set", "tuple", "bytes","sum", "round", "sorted","chr",
                "bin", "dir","vars","type","0","1","2","3","4","5","6","7","8","9"]
  
}

@app.route('/bank')
def get_Bank():
    return jsonify(SyntaxBank)

@app.route("/syntax")
def display():
    return render_template("SyntaxHighlighter.html")

if __name__ == '__main__':
    app.run(debug=True)