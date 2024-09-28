from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

with open('Dic_test.json', 'r', encoding='utf-8') as f:
    dictionary = json.load(f)

def hyperlink_words(meaning):
    words_in_meaning = meaning.split()
    for i, word in enumerate(words_in_meaning):
        clean_word = word.lower()
        if clean_word in dictionary:
            words_in_meaning[i] = f'<a href="#" class="linked-word" data-word="{clean_word}">{word}</a>'
    return ' '.join(words_in_meaning)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    word = request.form['word'].strip().lower()
    meaning = dictionary.get(word)
    if meaning:
        meaning_with_links = hyperlink_words(meaning)
        return jsonify({'word': word, 'meaning': meaning_with_links})
    else:
        return jsonify({'word': word, 'meaning': 'Word not found in the dictionary.'})

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query').lower()
    suggestions = [word for word in dictionary.keys() if word.startswith(query)]
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)