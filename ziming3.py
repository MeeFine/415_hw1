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
    print(introduce())
    while True:
        the_input = input('TYPE HERE:>> ')
        if match('bye',the_input):
            print('Goodbye! It\'s been a joy meeting you.')
            return
        respond(the_input, wordlist, mapped_wordlist)

def introduce():
    'Intro of this agent'
    str = "My name is " + agentName() + ", and I am a salesman."
    str += " I was programmed by Ziming Guo. If you don't like"
    str += " the way I deal, contact him at zimig3@uw.edu."
    str += " So how can I help you?"
    return str

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
        # Reaction to empty input.
    if 'fuck' in wordlist or 'fucking' in wordlist:
        fword_count = fword_count + 1
        if fword_count % 3 == 0:
            return 'Show some respect please.'
        elif fword_count % 3 == 1:
            return 'I don\'t like to hear the f word.'
        else:
            return 'This is not funny.'
        # When user use n word in their input.
    if wordlist[0] == 'hello' or wordlist[0] == 'hi':
        return 'Greetings.'
        # Greeting message.
    if wordlist[0:3] == ["how", 'are', 'you']:
        rand = random.randrange(3)
        if rand == 0:
            return 'I got so many business to do and so much money to make. I am busy and pleased.'
        elif rand == 1:
            return 'Today\'s good deals make me feeling very good'
        else:
            return 'I am sure I am having a good day.'
        # Reaction to question 'How are you'
    if wordlist[0:2] == ['i','am']:
        user.append("you are" + stringify(mapped_wordlist[2:]))
        return  "I am glad to hear more about you. Could you tell me why you are" +\
              stringify(mapped_wordlist[2:])
        # Record the user's personality. Will probably use it later.
    if wpred(wordlist[0]):
        return  "My knowledge is limited, I'd prefer to hear your opinion about "\
                + wordlist[0] + "."
        # Answer to When, Why, Where, How.
    if wordlist[0:2] == ['i','have']:
        return  "How long have you had " +\
              stringify(mapped_wordlist[2:]) + '.'
        # Answer to 'I have ...'
    if 'because' in wordlist:
        return  "Is this really the reason?"
        # Answer to input including 'because'
    if 'yes' in wordlist:
        return  "I am happy that you acknowledge my opinion."
        # Answer to inpout including 'yes'
    if wordlist[0:2] == ['you','are']:
        return  "I like to know how you think about me. " +\
              "Tell me why I am " + stringify(mapped_wordlist[2:]) + '.'
        # Answer to user's impression about the AI.
    if verbp(wordlist[0]):
        return  "If you want me to " +\
              stringify(mapped_wordlist) + ', you\'d better pay first.'
        # Answer to commands.
    if wordlist[0:3] == ['do','you','think']:
        return  "My opinion is minor, trust your own."
        # Answer to user asking for advices.
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        return  "I would like to " +\
                stringify(mapped_wordlist[2:]) + '.'
        # Answer to request.
    if 'dream' in wordlist:
        return  "I seldom dream."
        # Answer to input including 'dream'
    if 'love' in wordlist:
        return  "It's great that you have someone or something to love."
        # Answer to input including 'love'
    if 'no' in wordlist:
        return  "People sometimes make mistakes."
        # Answer to negation.
    if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
        recall = ''
        if user:
            rand = random.randrange(len(user))
            recall = 'You also told me that ' + user[rand] + '.'
        else:
            recall = 'I am interested in you, my potential customer. Tell me more.'
        index = 0
        if 'You' in mapped_wordlist:
            index = mapped_wordlist.index('You')
        if 'you' in mapped_wordlist:
            index = mapped_wordlist.index('you')
        user.append('you ' + stringify(mapped_wordlist[index+1:]))
        return recall
        # In this section, the agent will recall some topics that brought by user.
    return punt()
        # If any of the previous case is not covered, then return oen from PUNTS.

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

# main() # Launch the program.
