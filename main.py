from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('Dic_test.json', 'r', encoding='utf-8') as f:
    dictionary = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    word = request.form['word'].lower()
    meaning = dictionary.get(word, 'Word not found in the dictionary')
    return jsonify({'word': word, 'meaning': meaning})

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query', '').lower()
    suggestions = [word for word in dictionary if word.startswith(query)]
    return jsonify(suggestions[:5])

if __name__ == '__main__':
    app.run(debug=True)
