from flask import Flask
app = Flask(__name__)
@app.route('/')

def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert} ?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f'I like {adjective}{noun} ?'   

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if (number1.isdigit() == True):
        if(number2.isdigit() == True):
            return f'{number1} times {number2} is {int(number1)* int(number2)}'
        else:
            return 'Invalid inputs. Please try again by entering 2 numbers!'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if (n.isdigit() == True):
        i = int(n)
        f=''
        for x in range(0, i):
            f += word + ' '
        return f
            
    else:
        return 'Invalid input. Please try again by entering a word and a number!'


@app.route('/reverse/<word>/')
def reverse(word):
    f = ''
    for i in range(len(word)):
        f += word[(len(word)- i - 1)]
    return f

if __name__ == '__main__':
    app.run(debug=True)