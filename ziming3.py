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
            print('Goodbye! It\'s been a joy meeting you.')
            return
        respond(the_input, wordlist, mapped_wordlist)

def introduce():
    'Intro of this agent'
    print("My name is " + agentName() + ", and I am a salesman.")
    print("I was programmed by Ziming Guo. If you don't like")
    print("the way I deal, contact him at zimig3@uw.edu.")
    print("So how can I help you?")

def agentName():
    return "David"

user = []
fword_count = 0;

def respond(the_input):
    wordlist = split(' ',remove_punctuation(the_input))
        # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()
    if wordlist[0]=='':
        return  "Time is money, my friend. Say something, don't let me guess."
    if 'fuck' in wordlist or 'fucking' in wordlist:
        fword_count++
        if fword_count % 3 == 0:
            return 'Show some respect please.'
        elif fword_count % 3 == 1:
            return 'I don\'t like to hear the f word.'
        else:
            return 'This is not funny.'
    if wordlist[0] == 'hello' or wordlist[0] == 'hi':
        return 'Greetings.'
    if wordlist[0:3] == ["how", 'are', 'you']:
        rand = random.randrange(3)
        if rand == 0:
            return 'I got so many business to do and so much money to make. I am busy and pleased.'
        elif rand == 1:
            return 'Today\'s good deals make me feeling very good'
        else:
            return 'I am sure I am having a good day.'
    if wordlist[0:2] == ['i','am']:
        user.append(stringify(mapped_wordlist[2:]))
        return  "I am glad to hear more about you. Could you tell me why you are" +\
              stringify(mapped_wordlist[2:])
    if wpred(wordlist[0]):
        return  "My knowledge is limited, I'd prefer to hear your opinion about "\
                + wordlist[0] + "."
    if wordlist[0:2] == ['i','have']:
        return  "How long have you had " +\
              stringify(mapped_wordlist[2:]) + '.'
    if wordlist[0:2] == ['i','feel']:
        return  'I had the same feeling sometimes.'
    if 'because' in wordlist:
        return  "Is that really the reason?"
    if 'yes' in wordlist:
        return  "How can you be so sure?"
    if wordlist[0:2] == ['you','are']:
        return  "I like to know how you think about me. " +\
              "Tell me why I am " + stringify(mapped_wordlist[2:]) + '.'
    if verbp(wordlist[0]):
        return  "I am not your servant, why do I need to " +\
              stringify(mapped_wordlist) + 'as you commanded?'
    if wordlist[0:3] == ['do','you','think']:
        return  "My opinion is minor, trust your own."
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        return  "I would like to " +\
             stringify(mapped_wordlist[2:]) + '.'
    if 'dream' in wordlist:
        return  "I seldom dream."
    if 'love' in wordlist:
        return  "Love, how beautiful it is."
    if 'no' in wordlist:
        return  "People sometimes make mistakes."
    if 'maybe' in wordlist:
        return  "Be more decisive."
    if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
        return stringify(mapped_wordlist) + '.'
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
         'I am listening.']

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
