#from gpiozero import Servo
import time
sidedoorStatus = False
# Servo(pin number)
servo = Servo(25)

validUsers = dict()

def addUser(card, name=''):
    f = open("/users", "a")
    f.write(f'{card}: {name}')
    validUsers[card] = name

def switchLock():
    if sidedoorStatus: 
        servo.min()
    else: 
        servo.mid()

def popUserDict():
    f = open("/users", "r")
    for line in f:
        stmts = line.split(':')
        validUsers[stmts[0]] = stmts[1].lstrip().rstrip()

while(True):
    cardInfo = input()
    if cardInfo == '': continue
    if cardInfo == 'override':
        newCard = input()
        addUser(newCard)
    if validUsers.keys() == []:
        popUserDict()
    if cardInfo in validUsers.keys():
        switchLock()

# 0, 180, 90, respectively
servo.min()
servo.max()
servo.mid()
