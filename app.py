from flask import Flask, render_template, request, jsonify
import random

app = Flask(_name_)

# Initialize the secret number
secret_number = random.randint(1, 10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global secret_number
    guess = int(request.form['guess'])
    if guess < secret_number:
        return jsonify({'result': 'Too low!'})
    elif guess > secret_number:
        return jsonify({'result': 'Too high!'})
    else:
        secret_number = random.randint(1, 10)  # Reset the game
        return jsonify({'result': 'Correct! The number has been reset.'})

if _name_ == '_main_':
    app.run(debug=True,port=5003)
