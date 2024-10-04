from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

dictionary1 = load_dictionary('dic-1.json')
dictionary2 = load_dictionary('dic-2.json')
dictionary3 = load_dictionary('dic-3.json')

def hyperlink_words(meaning):
    if meaning:
        words_in_meaning = meaning.split()
        for i, word in enumerate(words_in_meaning):
            clean_word = word.lower()
            if clean_word in dictionary1 or clean_word in dictionary2 or clean_word in dictionary3:
                words_in_meaning[i] = f'<a href="#" class="linked-word" data-word="{clean_word}">{word}</a>'
        return ' '.join(words_in_meaning)
    return 'Meaning not found'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lookup', methods=['POST'])
def lookup():
    word = request.json.get('word').strip().lower()
    meaning1 = dictionary1.get(word, None)
    meaning2 = dictionary2.get(word, None)
    meaning3 = dictionary3.get(word, None)

    meanings = {
        'dictionary1': meaning1,
        'dictionary2': meaning2,
        'dictionary3': meaning3
    }

    meanings_with_links = {key: hyperlink_words(value) for key, value in meanings.items() if value}

    if not any(meanings_with_links.values()):
        return jsonify({'word': word, 'meanings': {}})

    return jsonify({'word': word, 'meanings': meanings_with_links})


@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query').lower()
    suggestions = set()

    for dictionary in [dictionary1, dictionary2, dictionary3]:
        suggestions.update([word for word in dictionary.keys() if word.startswith(query)])

    return jsonify(list(suggestions))

if __name__ == '__main__':
    app.run(debug=True)