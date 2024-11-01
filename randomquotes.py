from flask import Flask
import random
import os

app = Flask(__name__)

phrases = [
    "Get ready to be inspired…", 
    "See rejection as redirection.",
    "There is beauty in simplicity.",
    "You can’t be late until you show up.",
    "Maybe life is testing you. Don’t give up.",
    "Impossible is just an opinion.",
    "Alone or not you gonna walk forward.",
    "Can i be the only hope for you?",
    "'Cause I hate that it seems you were never enough Yeah, we're broken and bleeding in the name of love And I hope that we meet in another life I hope that we meet in another life I don't hate that I need you (I don't hate that I need you) I don't hate that I need you (I don't hate that I need you) I don't hate that I need you"
]

@app.route('/') 
def get_random_quote(): 
    phrase = random.choice(phrases) 
    container_id = os.uname()[1]  
    return f"{phrase} - Container Id: {container_id}" 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
