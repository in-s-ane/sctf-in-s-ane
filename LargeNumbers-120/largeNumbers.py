import math

x = 3466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
y = []
z = 3.14

m = "" #HIDDEN
n = ""
p = ""

# factors of x (excluding 1 and x)
factors = [13, 169, 4021, 52273, 71551, 679549, 930163, 12092119, 287706571, 3740185423, 48622410499, 71295471601695927997856535784841073199147573947838887511131682314427564225008537053688203655245421716621145609326460282847065961612226923304910779079974895230938063704799409598035363, 926841130822047063972134965202933951588918461321905537644711870087558334925110981697946647518190482316074892921243983677011857500958950002963840128039673638002194828162392324774459719, 12048934700686611831637754547638141370655939997184771989381254311138258354026442762073306417736476270108973607976171787801154147512466350038529921664515757294028532766111100222067976347, 286679091310419326479381130390845955333772394844260166682260494586313235748759327492880266897741840722533626495101696797328052231642764458609046242680579053723601954156998425993700194623, 3726828187035451244231954695080997419339041132975382166869386429622072064733871257407443469670643929392937144436322058365264679011355937961917601154847527698406825404040979537918102530099, 5101262288572945344174632991941163628472208063541820240308983001279606647863585834728444659736465169245959589492917559697990416619316448589389671153951283728668849396142102556149028258013, 48448766431460866175015411036052966451407534728679968169302023585086936841540326346296765105718371082108182877672186758748440827147627193504928815013017860079288730252532733992935332891287, 66316409751448289474270228895235127170138704826043663124016779016634886422226615851469780576574047200197474663407928276073875416051113831662065725001366688472695042149847333229937367354169, 862113326768827763165512975638056653211803162738567620612218127216253523488946006069107147495462613602567170624303067588960380408664479811606854425017766950145035547948015331989185775604197, 20512175662351813228926199260595418950086748623501659186282420648145298331059478641443075976800326445538003509351021507545619465226271439777935867710038111872977443421887394378275242625470273, 266658283610573571976040590387740446351127732105521569421671468425888878303773222338759987698404243791994045621563279598093053047941528717113166280230495454348706764484536126917578154131113549]

def a(b):
    '''
    Check if b is prime
    '''
    x = 2
    while (x < int(math.sqrt(b))):
        if b % x == 0:
            return False
        x += 1
    return True

def c(d):
    '''
    Find first factor of d that is a prime and add it to y; Let this factor be
    called f.
    Then, recurse with (d/f)
    y
    '''
    global y
    f = 2
    while not y and (f >= 2 and f < d):
        if d%f==0 and a(f):
            y = y + [f] + c(d/f) # c doesnt return anything so it is None -> error?
        f += 1

# First, let's calculate y because it is a constant
# ...
print str(y)
f = open("solution.txt", "w")
f.write(str(y))
f.close()

#if len(y) == 0:
#    c(x)
#
#for g in y:
#    z += g
#    z = math.sqrt(z)
#    z *= 1.1
#    z -= (g*0.1)
#    z = abs(z)
#
#n = ''.join(str(ord(q)) for q in m)
#
#for h in n:
#    if int(h) == 0:
#        p = p + repr(int(z/9999))
#    else:
#        p = p + repr(int(z/int(h)*999))
#
#p = p.replace("L",_) # Replace all L's with _
#p = p[:-1] # Remove last character
#print(p)
