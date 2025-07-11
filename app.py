from flask import Flask, render_template, request, jsonify
from pyswip import Prolog

app = Flask(__name__)
prolog = Prolog()

prolog.assertz("animal('ara', 'Ara Parrot', 'An endangered species of parrot native to Central and South America. Known for their bright colors and intelligence.')")
prolog.assertz("animal('white_stork', 'White Stork', 'A large bird, known for its long migrations from Europe to Africa. It is also a symbol of fertility.')")
prolog.assertz("plant('red_oak', 'Red Oak', 'A deciduous tree, native to North America. The leaves turn bright red in the fall and it is known for its strength and durability.')")

prolog.assertz("more_info('Ara Parrot', 'This parrot is often seen as a symbol of the tropical rainforests and is highly intelligent, often learning to mimic human speech.')")
prolog.assertz("more_info('White Stork', 'White storks are large birds known for their long migratory flights between Europe and Africa. They play a symbolic role in various cultures.')")
prolog.assertz("more_info('Red Oak', 'Red Oak trees are vital to the ecosystem, providing food and shelter to wildlife, and their wood is used in various products.')")

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/chat')
def model():
    return render_template('chat.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400

        print(f"Получено съобщение: {user_message}")

       
        if "Ara Parrot" in user_message:
            result = list(prolog.query("animal('ara', Name, Description)."))
        elif "White Stork" in user_message:
            result = list(prolog.query("animal('white_stork', Name, Description)."))
        elif "Red Oak" in user_message:
            result = list(prolog.query("plant('red_oak', Name, Description)."))
        elif "повече информация" in user_message:  # Търсене на допълнителна информация
            if "Ara Parrot" in user_message:
                more_info_result = list(prolog.query("more_info('Ara Parrot', Info)."))
            elif "White Stork" in user_message:
                more_info_result = list(prolog.query("more_info('White Stork', Info)."))
            elif "Red Oak" in user_message:
                more_info_result = list(prolog.query("more_info('Red Oak', Info)."))
            
            if more_info_result:
                return jsonify({'response': more_info_result[0]['Info']})

            return jsonify({'response': "I don't have more information on that."})

        else:
            return jsonify({'response': "I don't understand the question."})

        if result:
            return jsonify({'response': result[0]['Description']})

        return jsonify({'response': "I don't understand the question."})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
