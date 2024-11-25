from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

SyntaxBank = {
    "operators": ["+", "-", "*", "/", "=", "<", ">", "(", ")", "{", "}", "++", "--"],
    "keywords" : ["for","while","if", "else","elif", "in"],
    "litfun" : ["int", "print", "float", "range", "len", "string", "bool","dict",
                "str","list","set", "tuple", "bytes","sum", "round", "sorted","chr",
                "bin", "dir","vars","type"]
  
}
 #Checks if 'word' is number
def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        return False

#Add 'word' to SyntaxBank if it's not already there
def add_to_litfun(word):
    if word not in SyntaxBank['litfun']:
        SyntaxBank['litfun'].append(word)

#                               *** _____Routing Section____***

@app.route('/')
def index():
    return render_template('SyntaxHighlighter.html')
    

@app.route('/syntax', methods=['GET'])
def get_Bank():
    return jsonify(SyntaxBank)

@app.route('/process_word', methods=['POST','GET'])
def process_word():
    data = request.json  
    word = data.get('word')
    
    #Word Checker
    if word:
        found_in_category = None
        
        if is_number(word):
            found_in_category = "litfun"
            add_to_litfun(word)
            
        for category, words_list in SyntaxBank.items():
            if word in words_list:
                found_in_category = category
                break


        if found_in_category:
            return jsonify({
                'message': f"Found word: '{word}' in category: {found_in_category}",
                'word': word,
                'is_found': True,
                'category': found_in_category
                
        
            }), 200
        else:
            return jsonify({
                'message': f"Word '{word}' not found in any category",
                'word': word,
                'is_found': False,
                'category': None  # No category
                }),200   
    else:
       
        return jsonify({'error': 'Not keyword'}), 400

    

if __name__ == '__main__':
    app.run(debug=True)
    
