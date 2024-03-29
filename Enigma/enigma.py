import codecs
import time

marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_◦ +1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'''


def sip(s1, s2, s1s2):  # s1s2 text that will be changed
    enc = s1s2.maketrans(s1, s2)
    s3 = s1s2.translate(enc)
    return s3.upper()


def shift(step, stroka):
    res = (stroka[-step:] + stroka[:-step])
    return res


def text_cleaner():
    with codecs.open("dirty_text.txt", encoding='utf-8') as f:
        text = f.read()
    for i in text:
        if i in marks:
            text = text.replace(i, "")
    with codecs.open("clear_text.txt", "w", encoding='utf-8') as f1:
        f1.write(text)


start_time = time.time()
print("--------------------------------------------------------------------")
print("This's working prototype of Enigma 3M by Oganes Bozoyan " + '\n')
print("Choose mode : keyboard(1) or file(2). To exit type 'q'" + '\n')
while 1:
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    reflector1 = 'СЗЭЧХЮЖЁФПЫВНИКТЛШМРЩДУЙЬГЯЪЕАБОЦ'  # here you can put any key as you want
    rot1 = 'ИДЦБШЧРЮФУЕВСОЙМПНТЁЯАГЬЩЗЫКЭЖХЪЛ'  # here you can put any key as you want
    rot2 = 'ДШЗВГЬПЕЁЙЫИЯЦЭФЮСХАОЧНБУКРТМЩЛЪЖ'  # here you can put any key as you want
    rot3 = 'СЪВЩДФЙБЧЫПХМЦЖКРЁУИГЗОТАНЯЭЮШЬЛЕ'  # here you can put any key as you want
    plugboard = 'ЯЬВРДЁЕЖТИЙКЛШНОПГСЗХФУЦЧМЩЪЮБЭЫА'  # here you can put any key as you want
    counter_1 = -1
    counter_2 = -1
    counter_3 = -1
    pluging = []
    letter = []
    kep = 0
    mode = input('Your mode: ')
    print('\n')
    if mode == '1':
        text = input("Type your text ,if you want to stop,just type 'stop' : ")

        for i in text:
            if i in marks:
                text = text.replace(i, "")
        print("text cleaned of marks")
        if text == 'stop':
            print("shutting down...")
            exit()
        else:
            ysl = len(text)
            print("Here is your encrypted text :")
            for i in range(ysl):
                pluging.append(sip(alph, plugboard, str(text[i])))
                letter = pluging[i]
                rot1 = shift(kep, rot1)
                R = sip(alph, rot1, str(letter))
                letter = R
                if (rot1[0] == 'И'):
                    counter_2 += 1
                rot2 = shift(counter_2, rot2)
                counter_2 = 0
                M = sip(alph, rot2, str(letter))
                letter = M
                if (rot2[0] == 'Д'):
                    counter_3 += 1
                rot3 = shift(counter_3, rot3)
                counter_3 = 0
                L = sip(alph, rot3, str(letter))
                letter = L
                U = sip(alph, reflector1, str(letter))
                letter = U
                L_1 = sip(rot3, alph, str(letter))
                letter = L_1
                M_1 = sip(rot2, alph, str(letter))
                letter = M_1
                R_1 = sip(rot1, alph, str(letter))
                letter = R_1
                P_1 = sip(plugboard, alph, str(letter))
                letter = P_1
                kep = (counter_1 + 3 - 1)
                print(letter, end='')
            print()
            print("--- %s seconds ---" % (time.time() - start_time))
    elif mode == '2':
        print("Your text must be in dirty_text.txt" + '\n')
        clearing = text_cleaner()
        print("I've remove from your text all this symbols : \n")
        print('''!()-[]{};?@#$%:'"\,./^&amp;*_ +1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz''',
              end='\n\n')
        with codecs.open("clear_text.txt", encoding="utf-8") as f:
            lista = f.read()
        ysl = len(lista)
        print("Here is your encrypted text :", end='\n\n')
        for i in range(ysl):
            pluging.append(sip(alph, plugboard, str(lista[i])))
            letter = pluging[i]
            rot1 = shift(kep, rot1)
            R = sip(alph, rot1, str(letter))
            letter = R
            if (rot1[0] == 'И'):
                counter_2 += 1
            rot2 = shift(counter_2, rot2)
            counter_2 = 0
            M = sip(alph, rot2, str(letter))
            letter = M
            if (rot2[0] == 'Д'):
                counter_3 += 1
            rot3 = shift(counter_3, rot3)
            counter_3 = 0
            L = sip(alph, rot3, str(letter))
            letter = L
            U = sip(alph, reflector1, str(letter))
            letter = U
            L_1 = sip(rot3, alph, str(letter))
            letter = L_1
            M_1 = sip(rot2, alph, str(letter))
            letter = M_1
            R_1 = sip(rot1, alph, str(letter))
            letter = R_1
            P_1 = sip(plugboard, alph, str(letter))
            letter = P_1
            kep = (counter_1 + 3 - 1)
            print(letter, end='')
        print()
        print("--- %s seconds ---" % (time.time() - start_time))
    elif mode == 'q':
        print("--- %s seconds ---" % (time.time() - start_time))
        quit()
