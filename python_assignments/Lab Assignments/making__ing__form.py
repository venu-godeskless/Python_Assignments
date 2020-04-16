"""
In English, present participle is formed by adding suffix -ing to infinite form: go -
> going. A simple set
of heuristic rules can be given as follows:
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee,
etc.)
If the verb ends in ie, change ie to y and add ingFor words consisting of consonant-vowel-consonant, double the final letter before
adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb
in infinitive form
returns its present participle form. Test your function with words such as lie, see,
move and hug.
"""




def make_ing_form(verb):
    v3 = verb[-2:]
    x=verb[-2:]
    y=verb[-1:]
    # return verb[-3],verb[-2],verb[-1]
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels='aeiou'

    if v3 == 'ee':
        return verb + 'ing'

    elif x == 'ie': 
        new=verb[:-2]
        return new+'ying'

    elif y=='e':
        new=verb[:-1]
        return new+'ing'

    elif verb[-1] == 'y':
        return verb+'ing'

    elif verb[-3] in consonants and verb[-2] in vowels and  verb[-1] in consonants:
        return verb+verb[-1]+'ing'

    else:
        return verb+'ing'

# x='die'
# x='be'
# x='move'
# x='study'
# x='see'
x=['lie', 'see', 'move', 'hug', 'study','work','lunch','write','watch','play','enjoy','fancy','wait','hold','stop','add']
for str in x:
    print(make_ing_form(str))
