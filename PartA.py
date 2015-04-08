def six_x_cubed_plus_5(x):
    return 6 * (x ** 3) + 5

def mystery_code(str, num):
    ans = ""
    for c in str:
        ans = ans + chr(ord(c) ^ num)
    return ans

def quadruples(seq):
    subl = len(seq) // 4
    subs = []
    for i in range(subl):
    	subs.append(seq[(4*i):(4*i)+4])
    if len(seq) % 4 != 0:
        i = i + 1
        subs.append(seq[4*i:4*i+len(seq)%4])
    return subs

def past_tense(list):
    past = []
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowel = ["a", "e", "i", "o", "u"]
    irreg = {"eat":"ate", "go":"went", "is":"was", "am":"was", "are":"were", "have":"has"}
    for i,v in enumerate(list):
        length = len(v)
        if (v in irreg.keys()):
            past.append(irreg[v])
        elif (v[length-1] == "e"):
            past.append(v + "d")
        elif (v[length-1] == "y" and (v[length-2] in consonant)):
            past.append(v[:length-1] + "ied")
        elif ((v[length-1] in consonant) and (v[length-2] in vowel) and (v[length-3] not in vowel)):
            past.append(v + v[length-1] + "ed")
        else:
            past.append(v + "ed")
    return past

