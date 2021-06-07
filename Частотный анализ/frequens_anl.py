import string
import codecs
print('\n')
print("Frequency analysis for Russian Language in 'Text' file")
k = 0
alph_rus = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
alph_rus_big = [x.capitalize() for x in alph_rus]
statistik =[7.998,1.592,4.533,1.687,2.977,8.483,0.013,0.94,1.641,7.367,1.208,3.486,4.343,3.203,6.7,10.983,2.804,4.746,5.473,6.318,2.615,0.267,0.966,0.486,1.45,0.718,0.361,0.037,1.898,1.735,0.331,0.638,2.001]
for j in range(33):
    statistik[j] = round(statistik[j],2)
    k +=1
k = 0
print(statistik)
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
proc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #array for calc of procent of letters in text
print(len(proc))
print(len(statistik))
print('\n')#Let's
print("Loading alphabit...")#Make
print('')#Some
print('3...')#cosmetics
print('')#weeeee
print('2...')#are
print('')#we 
print('1...')#we'll
print('')#rock
print(alph_rus_big)#you
print('\n')#i
print(alph_rus)#belive
print('\n')#i
print("Done")#can
print('\n')#fly
print("What's name of your file ? :")#i
print('')#belive
file = input()
print('')
f = codecs.open(file,encoding='utf-8')
size = 0 #we will measure the value of letters in file
for i in f.read():
    if i.lower() == alph_rus[0] or i.lower() == alph_rus_big[0]:
        count[0] += 1
        size += 1
    elif i.lower() == alph_rus[1] or i.lower() == alph_rus_big[1]:
        count[1] += 1
        size += 1
    elif i.lower() == alph_rus[2] or i.lower() == alph_rus_big[2]:
        count[2] += 1
        size += 1
    elif i.lower() == alph_rus[3] or i.lower() == alph_rus_big[3]:
        count[3] += 1
        size += 1
    elif i.lower() == alph_rus[4] or i.lower() == alph_rus_big[4]:
        count[4] += 1
        size += 1
    elif i.lower() == alph_rus[5] or i.lower() == alph_rus_big[5]:
        count[5] += 1
        size += 1
    elif i.lower() == alph_rus[6] or i.lower() == alph_rus_big[6]:
        count[6] += 1
        size += 1
    elif i.lower() == alph_rus[7] or i.lower() == alph_rus_big[7]:
        count[7] += 1
        size += 1
    elif i.lower() == alph_rus[8] or i.lower() == alph_rus_big[8]:
        count[8] += 1
        size += 1
    elif i.lower() == alph_rus[9] or i.lower() == alph_rus_big[9]:
        count[9] += 1
        size += 1
    elif i.lower() == alph_rus[10] or i.lower() == alph_rus_big[10]:
        count[10] += 1
        size += 1
    elif i.lower() == alph_rus[11] or i.lower() == alph_rus_big[11]:
        count[11] += 1
        size += 1
    elif i.lower() == alph_rus[12] or i.lower() == alph_rus_big[12]:
        count[12] += 1
        size += 1
    elif i.lower() == alph_rus[13] or i.lower() == alph_rus_big[13]:
        count[13] += 1
        size += 1
    elif i.lower() == alph_rus[14] or i.lower() == alph_rus_big[14]:
        count[14] += 1
        size += 1
    elif i.lower() == alph_rus[15] or i.lower() == alph_rus_big[15]:
        count[15] += 1
        size += 1
    elif i.lower() == alph_rus[16] or i.lower() == alph_rus_big[16]:
        count[16] += 1
        size += 1
    elif i.lower() == alph_rus[17] or i.lower() == alph_rus_big[17]:
        count[17] += 1
        size += 1
    elif i.lower() == alph_rus[18] or i.lower() == alph_rus_big[18]:
        count[18] += 1
        size += 1
    elif i.lower() == alph_rus[19] or i.lower() == alph_rus_big[19]:
        count[19] += 1
        size += 1
    elif i.lower() == alph_rus[20] or i.lower() == alph_rus_big[20]:
        count[20] += 1
        size += 1
    elif i.lower() == alph_rus[21] or i.lower() == alph_rus_big[21]:
        count[21] += 1
        size += 1
    elif i.lower() == alph_rus[22] or i.lower() == alph_rus_big[22]:
        count[22] += 1
        size += 1
    elif i.lower() == alph_rus[23] or i.lower() == alph_rus_big[23]:
        count[23] += 1
        size += 1
    elif i.lower() == alph_rus[24] or i.lower() == alph_rus_big[24]:
        count[24] += 1
        size += 1
    elif i.lower() == alph_rus[25] or i.lower() == alph_rus_big[25]:
        count[25] += 1
        size += 1
    elif i.lower() == alph_rus[26] or i.lower() == alph_rus_big[26]:
        count[26] += 1
        size += 1
    elif i.lower() == alph_rus[27] or i.lower() == alph_rus_big[27]:
        count[27] += 1
        size += 1
    elif i.lower() == alph_rus[28] or i.lower() == alph_rus_big[28]:
        count[28] += 1
        size += 1
    elif i.lower() == alph_rus[29] or i.lower() == alph_rus_big[29]:
        count[29] += 1
        size += 1
    elif i.lower() == alph_rus[30] or i.lower() == alph_rus_big[30]:
        count[30] += 1
        size += 1
    elif i.lower() == alph_rus[31] or i.lower() == alph_rus_big[31]:
        count[31] += 1
        size += 1
    elif i.lower() == 'я' or i.lower() == 'Я':
        count[32] += 1
        size += 1
    
print(count)
print('')
print("Value of characters in text :")
print('')
print(size)
print('')

for z in range(33):
    proc[z] = (int(count[k])*100)/size#filling array of procents
    proc[z] = round(proc[z],2)
    k +=1
print("Procent of frequens you can see below or in 'proc_of_letters.txt' file")
print('')
print(proc)
of = codecs.open("proc_of_letters.txt" , "w",encoding='utf-8')
of.write('Here is frequens of letters in "' +str(file)+'\"'+'\n'+'First column is statistic percent in second the letter and in third percentage of this text'+'\n')
for x in range(33):
    
    of.write(str(statistik[x])+'|'+str(alph_rus[x])+'|'+str(proc[x])+'\n')#filling proc_of_letters.txt with our procents
    x+=1
of.close()
f.close()
