# ziming3.py
# A conversational "doctor" simulation modelled loosely
# after J. Weizenbaum's ELIZA.
# This Python program goes with the book "The Elements of Artificial
# Intelligence".
# This version of the program runs under Python 3.x.

# Steven Tanimoto
# (C) 2012.

from re import *   # Loads the regular expression module.
import random

def main():
    "This is the main function"
    introduce()
    while True:
        the_input = input('TYPE HERE:>> ')
        if match('bye',the_input):
            rand = random.randrange(4)
            if (rand == 0):
                print('Goodbye!')
            elif (rand == 1):
                print('May magic protect you.')
            elif (rand == 2):
                print('Never temper your passion.')
            else:
                print('Remember Theramore.')
            return
        respond(the_input, wordlist, mapped_wordlist)

def introduce():
    'Intro of this agent'
    print("My name is " + agentName() + ", and I am a taxi driver.")
    print("I was programmed by Ziming Guo. If you don't like")
    print("the way I deal, contact him at zimig3@uw.edu.")
    print("So what is your problem?")

def agentName():
    return "David Angry"

def respond(the_input):
    wordlist = split(' ',remove_punctuation(the_input))
        # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()
    if wordlist[0]=='':
        return  "Don't waste my time, tell me what you want to say!"
    if wordlist[0] == 'hello' or wordlist[0] == 'hi':
        return 'Greetings.'
    if wordlist[0:3] == ["how", 'are', 'you']:
        return 'I got so much things to do, but I am forced' + \
               ' to talk with you, guess how do I feel?'    
    if wordlist[0:2] == ['i','am']:
        return  "I am not interested in why you are " +\
              stringify(mapped_wordlist[2:]) + ' at all.'
    if wpred(wordlist[0]):
        return  "I am just a taxi driver, how could I possibly know "\
                + wordlist[0] + "."
    if wordlist[0:2] == ['i','have']:
        return  "How long have you had " +\
              stringify(mapped_wordlist[2:]) + '.'
    if wordlist[0:2] == ['i','feel']:
        return  "I don't really care how you feel."
    if 'because' in wordlist:
        return  "Is that really the reason?"
    if 'yes' in wordlist:
        return  "How can you be so sure?"
    if wordlist[0:2] == ['you','are']:
        return  "You just know me, it's  " +\
              stringify(mapped_wordlist[2:]) + '.'
    if verbp(wordlist[0]):
        return  "I am not your servant, why do I need to " +\
              stringify(mapped_wordlist) + 'as you commanded?'
    if wordlist[0:3] == ['do','you','think']:
        return  "I don't know, I am not your professor."
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        return  "Perhaps I " + wordlist[0] + ' ' +\
             stringify(mapped_wordlist[2:]) + '.'
    if 'dream' in wordlist:
        return  "For dream analysis see Freud."
    if 'love' in wordlist:
        return  "All's fair in love and war."
    if 'no' in wordlist:
        return  "Don't be so negative."
    if 'maybe' in wordlist:
        return  "Be more decisive."
    if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
        answer = stringify(mapped_wordlist) + '.'
    return punt()

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

PUNTS = ['Please go on.',
         'Tell me more.',
         'I see.',
         'What does that indicate?',
         'But why be concerned about it?',
         'Just tell me how you feel.']

punt_count = 0
def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])

main() # Launch the program.
