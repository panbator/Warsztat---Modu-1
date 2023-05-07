from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def imagine_number():
    if request.method == 'POST':
        min = int(request.form['min'])
        max = int(request.form['max'])
        guess = int((max - min) / 2) + min
        try:
            user_response = request.form['user_response']
            if user_response not in ['Too big', 'Too small', 'You win']:
                raise ValueError("Invalid input, please type one of the answers.")
        except ValueError:
            return render_template('error.html')

        session_tries = session.get('session_tries', 1)
        session_tries += 1
        session['session_tries'] = session_tries

        if user_response == 'Too big':
            max = guess
        elif user_response == 'Too small':
            min = guess
        elif user_response == 'You win':
            return render_template('win.html')

        guess = int((max - min) / 2) + min

        if session_tries >= 10:
            return render_template('cheated.html')

    else:
        min = 0
        max = 1000
        guess = int((max - min) / 2) + min
        session['session_tries'] = 0

    return render_template('index.html', min=min, max=max, guess=guess)


if __name__ == '__main__':
    app.run(debug=True)