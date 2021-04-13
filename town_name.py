import random
import requests

alpha = ['x', 'q', 'j', 'z', 'k', 'v', 'b', 'p', 'p', 'g', 'g', 'w', 'w', 'y', 'y', 'f', 'f', 'm', 'm', 'm', 'c', 'c',
         'c', 'u', 'u', 'u', 'd', 'd', 'd', 'd', 'l', 'l', 'l', 'l', 's', 's', 's', 's', 's', 's', 'r', 'r', 'r', 'r',
         'r', 'r', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'o', 'o', 'o', 'o', 'o', 'o',
         'o', 'o', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'e', 'e', 'e',
         'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
town_end = ['boro', 'ward', 'holm', 'firth', 'fjord', 'strom', 'mire', 'strand', 'fell', 'thorpe', 'keld', 'kirk',
            'mouth', 'land', 'hammar', 'vik', 'heim', 'port', 'clare', 'ley', 'view', 'folk', 'karta', 'grad',
            'hampton', 'stead', 'stedt', 'stätt', 'dorf', 'wych', 'wick', 'wich', 'thorpe', 'ham', 'cester', 'stadt',
            'caster', 'by', 'dale', 'field', 'ford', 'town', 'bury', 'chester', 'ton', 'burgh', 'burg', 'ville']
a = 0
while a != 20:
    name = ''
    length = random.randint(3, 6)
    for x in range(0, length):
        name = (name + alpha[random.randint(0, (len(alpha)) - 1)])
    if requests.head(('https://www.dictionary.com/browse/' + name + '?s=t')).status_code == 200:
        ing = random.randint(0, 100)
        a = (a + 1)
        if ing < 15:
            print(name + 'ing' + town_end[random.randint(0, (len(town_end)) - 1)])
        else:
            print(name + town_end[random.randint(0, (len(town_end)) - 1)])
    else:
        continue
