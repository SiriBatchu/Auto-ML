from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global target_number
    guess = int(request.json['guess'])
    if guess < target_number:
        return jsonify({'message': 'Too low!'})
    elif guess > target_number:
        return jsonify({'message': 'Too high!'})
    else:
        target_number = random.randint(1, 100)  # Reset the game
        return jsonify({'message': 'Correct! You guessed the number!'})

if __name__ == '__main__':
    app.run(debug=True)
