from tkinter import *
import array


width = 1200
height = 700
wbase = 10
hbase = 100
rectWidth = 110
rectHeight = 50
color = "blue"


root = Tk()
canvas = Canvas(root,width = width, height= height)





#For Entity Extra



def count_relation(en,M,R1,R2):

    for dest in range(en-1,-1,-1):
        for src in range(dest):
            if src % 2 == 0 and M[src][dest] == 1:
                R1[dest] += 1
            elif M[src][dest] == 1:
                R2[dest] += 1
                


def init_entity(en):
    list = []
    
    for i in range(en):
        ename = "Entity"
        ename += str(i+1)
        list.append(ename)

    return list



def draw_Relation(en,M,wdiv,hdiv):

    global canvas
    src = int

    flag = 0

    if en % 2 != 0:
        flag = 1
        
    rWidth = rectWidth

    L1 = array.array('i',(0 for j in range((en+1)//2)))
    L2 = array.array('i',(0 for j in range((en+1)//2)))
    
    

    
    for src in range(en):
        for dest in range(en):
            if src == dest:
                continue

            if M[src][dest] == -1 or M[dest][src] == -1:
                continue
            diff = dest - src
            line = diff/2
            k = wdiv/4*3

            
            if src%2 == 0:
                if diff != 1 and dest%2 != 0:
                    L2[dest//2] += 1
            else:
                if dest+1 % 2 != 0:
                    L1[dest//2] += 1

            print(L1)
            print('src = ',src,'dest = ',dest)

            if src%2 == 0:

                #For drawing the diamonds
                if en % 2 != 0 and dest+1 == en:
                    pX1 = (dest//2+1)*wdiv + dest//2*rectWidth
                    pY1 = ((height-50)/2)-15
                elif diff < 2:
                    pX1 = (src/2+1)*wdiv+(src/2*rectWidth)+rectWidth/2
                    pY1 = hdiv-15
                elif (diff-1) % 2 == 0:
                    pX1 = (dest//2+1)*wdiv + (dest//2)*rectWidth
                    pY1 = hdiv-15
                    if L2[dest//2]-1 > 0:
                        pX1 = pX1+(L2[dest//2]-1)*5+(L2[dest//2]-1)*15

                else :
                    if diff == 2:
                        pX1 = (src//2+1)*(wdiv+rectWidth)+wdiv/2
                        pY1 = hbase+rectHeight/2-7.5
                    else :
                        pX1 = (dest//2)*(wdiv+rectWidth)+wdiv
                        pY1 = hbase-15

                #For drawing lines
                if en % 2 != 0 and dest+1 == en:
                    SX1 = (src/2+1)*(wdiv+rectWidth)
                    SY1 = hbase+rectHeight
                    SX2 = (dest/2)*(wdiv+rectWidth)+wdiv
                    SY2 = (height-50)/2-15
                elif diff < 2:
                    SX1 = (src//2+1)*wdiv+src//2*rectWidth+rectWidth/2
                    SY1 = hbase+rectHeight
                    SX2 = SX1
                    SY2 = height-hbase-rectHeight-14

                else:
                    if diff/2 == 1:
                        SX1 = (src//2+1)*(wdiv+rectWidth)
                        SY1 = hbase+rectHeight/2
                        SX2 = SX1+wdiv/2
                        SY2 = SY1
                        canvas.create_line(SX1, SY1, SX2-5, SY2)
                        SX1 = SX2 + 5
                        SX2 = SX1+wdiv/2-5
                    elif (diff+1)%2 == 0:
                        SX1 = (src+1)*(wdiv+rectWidth)
                        SY1 = hbase+rectHeight
                        SX2 = SX1+(diff//2-1)*(wdiv+rectWidth)+wdiv
                        SY2 = height-hbase-rectHeight-14

                M[src][dest] = -1
                M[dest][src] = -1

                    
            else:
                #For relation
                if en % 2 != 0 and dest + 1 == en:
                    pX1 = (dest//2+1)*wdiv + dest//2*rectWidth
                    pY1 = (height-50)/2+rectHeight
                elif diff % 2 != 0:
                    pX1 = (dest//2+1)*wdiv+(dest//2)*rectWidth
                    pY1 = hbase+rectHeight
                    if L1[src//2]-1 > 0:
                        pX1 += (L1[dest//2]-1)*15
                else :
                    if diff == 2:
                        pX1 = (src//2+1)*(wdiv+rectWidth)+wdiv/2
                        pY1 = hdiv + rectHeight/2
                    else :
                        pX1 = (dest//2)*(wdiv+rectWidth)+wdiv
                        pY1 = hdiv + rectHeight

                #For line
                if en % 2 != 0 and dest+1 == en:
                    SX1 = src*(wdiv+rectWidth)
                    SY1 = height-hbase-rectHeight
                    SX2 = dest/2*(wdiv+rectWidth)+wdiv
                    SY2 = (height-50)/2+rectHeight+15
                elif diff % 2 == 0:
                    if diff == 2:
                        SX1 = (src)*(wdiv+rectWidth)
                        SY1 = height-hbase-rectHeight/2+7.5
                        SX2 = SX1+wdiv/2
                        SY2 = SY1
                        canvas.create_line(SX1, SY1, SX2-5, SY2)
                        SX1 = SX2 + 5
                        SX2 = SX1+wdiv/2-5

                else :
                    SX1 = src*(wdiv+rectWidth)
                    SY1 = height-hbase-rectHeight+7.5
                    SX2 = (dest-1)*(wdiv+rectWidth)+wdiv
                    SY2 = hbase+rectHeight+15
                        
                M[src][dest] = -1
                M[dest][src] = -1

            pX2 = pX1
            pY2 = pY1 + 15

            pX3 = pX1 - 5
            pY3 = pY1 + (15/2)

            pX4 = pX1 + 5
            pY4 = pY3

            canvas.create_polygon(pX1,pY1,pX4,pY4,pX2,pY2,pX3,pY3,fill = color)
            canvas.create_line(SX1, SY1, SX2, SY2)



def draw_ER(entity, entityList,M):

    total = (int)(entity/2) + (entity%2)
    wdiv = (width - (total * rectWidth))/(total + 1)
    hdiv = height - (hbase + rectHeight)
    
    rect1X = wdiv
    rect1Y = hbase
    rect2X = rect1X + rectWidth
    rect2Y = rect1Y + rectHeight

    
    global canvas
    
    root.title("ER diagram")
    canvas.pack()

    #canvas.create_rectangle(10,20,120,70)

    for i in range(entity - (entity % 2)):
        canvas.create_rectangle(rect1X,rect1Y,rect2X,rect2Y)
        canvas.create_text(rect1X+(rectWidth/2), rect1Y+(rectHeight/2),
                           text=entityList[i],fill = "red")
        if(i+1) % 2 != 0:
            rect1Y  = hdiv

        if(i+1) % 2 == 0:
            rect1X += (wdiv + rectWidth)
            rect1Y = hbase

        rect2X = rect1X + rectWidth
        rect2Y = rect1Y + rectHeight

    for i in range(entity%2):
        rect1Y = (height - 50) / 2
        rect2X = rect1X + rectWidth
        rect2Y = rect1Y + rectHeight
        canvas.create_rectangle(rect1X,rect1Y,rect2X,rect2Y)
        canvas.create_text(rect1X+(rectWidth/2), rect1Y+(rectHeight/2),
                           text=entityList[entity-1],fill = "red")

            
    #canvas.create_polygon(pX1,pY1,pX4,pY4,pX2,pY2,pX3,pY3,fill = color)

    draw_Relation(entity,M,wdiv,hdiv)        

    root.mainloop()


    








#Removes end s ,ies of a word
def modifyEntity(word):
    
    l = len(word)
    if (l>3):
        if word[l-1] == 's':
            if word[l-3:l] == 'ies':
                word = word[0:l-3]+'y'
            else:
                word = word[0:l-1]

    
       
    return word

#Checks for possible entities
def checkEntity(word):

    checkList = ['A','a','An','AN','an','THE','The','the','EACH','Each','each','all','All']

    for check in checkList:
        if check == word:
            return True

    return False

#Checks for attributes
def checkEntity2(word):

    checkList = ['identified','described','defined']

    for check in checkList:
        if check == word:
            return True

    return False

print ("Enter the statement:\n")

statement = input()
statement = statement.lower()
statement2= statement  #copy the statement into another string

#Split the text into sentences
lines = statement.split('.')
lines2 = statement.split('.')
#removes comma from sentence
for i in range(len(lines)):
    lines[i] = lines[i].replace(',',' ')
    #print (lines[i])

entities = []

for i in lines:

    #split into words
    words = i.split()

    count = 0
    flag = 0
  #Considering that the entity should be with in the fisrt four words  
    for word in range(len(words)):
        count += 1
        flag = 0 
        if checkEntity(words[word]):
            entities.append(words[word+1])
            flag = 1
            break
        if count == 6: #Entity must appear in first 6 words
            if flag == 0:           #Check the first word
                entities.append(words[0])    
            break
        

for j in range(len(entities)):
    entities[j] = modifyEntity(entities[j])
'''
#List of possible entities including duplicates
print ("Possible Entities:")
print()
for entity in entities:
    print (entity)
'''
print ()

#remove duplicates
entities = list(set(entities))

print ("Possible entities are :")
print()
for entity in entities:
    print (entity)
    #print (len(entity))


realentities = []
attr = []
temp = []
#for attributes
count = 0
co = 0
for i in lines2:

    #split into words
    words = i.split()




    
    k = 0
    list10 = []
    count=0
  #Considering that the entity should be with in the fisrt four words  
    for word in range(len(words)):
        if checkEntity2(words[word]):
            realentities.append(words[word-2])
            count  = word-2
            word = word+2
            count = count + 1
            for k in range(len(words)-word):
                if (words[k+word]!=','):
                    attr.append(words[k+word])
                    
                    count = count + 1
                    
                
            attr.append('||')
            break
   

count = 0
#print ('attr',attr)
l=len(realentities)
names = []
list10 = []

    
#print(realentities)
for j in range(len(realentities)):
    realentities[j] = modifyEntity(realentities[j])

print()
print('entitties are ',realentities)
print()
#print(attr)
kl = 0
print ('aatribues of ',realentities[kl],' are ')
for kj in range(len(attr)):
    
    if (attr[kj]!='||'):
        print(' ',attr[kj])
    elif (kj!=len(attr)):
        kl=kl+1
        if(kl>= len(realentities)):
            break
        else:
           print ('atributes of ',realentities[kl],' are ')
print()

          



entityList = realentities
en = len(entityList)
#print(entityList)




#For Relationship between entites

length = len(realentities)
print(length)
R = [[0 for x in range(length)]for y in range(length)]

lines3 = statement.split('.')

#removes comma from sentence
for i in range(len(lines3)):
    
    lines3[i] = lines[i].replace(',',' ')
#    print (lines3[i])
list8 = []
for i in range(len(lines3)):
    
    array1 = lines3[i].split()
#    print(array)
    for j in range(len(array1)):
        array1[j] = modifyEntity(array1[j])
#    print(array)
    list8.append(array1)

#print(list8)
for i in range(len(list8)):
    a=list8[i]
    #print(i,a)
    row=-1
    col=-1
    for j in range(len(realentities)):
        if realentities[j] in a:
            row = j
            break
    if row != -1:
        for m in range(len(realentities)-row-1):
            if realentities[m+row+1] in a:
                col = m+row+1
                break
    if (row != -1 and col != -1):
        #print(row,col)
        R[row][col]=1
        R[col][row]=1
''' 

for i in range(length):
    for j in range(length):
        print (R[i][j])
    print('\n')
'''


for i in range(length):
    for j in range(length):
        print (R[i][j],end = ' ')
    print()      





M = [[0 for x in range(en)] for y in range(en)]


for i in range(en):
    for j in range(en):
        if R[i][j] == 1:
            M[i][j] = 1
        else:
            M[i][j] = -1

'''
for i in range(en):
    for j in range(en):

        if i == j:
            continue
        if M[i][j] == 1:
            continue
        if M[i][j] == -1 or M[j][i] == -1:
            continue
        
        print ("Is there any relation between "+entityList[i] +
               " and "+entityList[j]+"?(Y/N) : ")
        ans = input()
        
        if ans == 'Y'  or ans == 'y':
            M[i][j] = 1
            M[j][i] = 1
        elif ans == 'N' or ans == 'n':
            M[i][j] = -1
            M[j][i] = -1
        else:
            print("please enter a valid answer.")
            
for i in range(en):
    for j in range(en):
        print (M[i][j],end = ' ')
    print()      '''



draw_ER(en, entityList,M)
