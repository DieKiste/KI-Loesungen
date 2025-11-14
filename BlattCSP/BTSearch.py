class CSP:
    def __init__(self):
        self.constraints = [] 
        self.needs2Houses = False
    def consistent(self, house1, house2):
        if not self.needs2Houses:
            for c in self.constraints:
                if not c(house1):
                    return False
        else:
            for c in self.constraints:
                if not c(house1, house2):
                    return False
        return True
        

class House:
    def __init__(self):
        self.number = None
        self.color = None
        self.nationality = None
        self.pet = None
        self.drink = None
        self.cigarres = None

def BTSearch():
    pass


houses = [House() for i in range(5)]
numbers = [1,2,3,4,5]
colors = ["gelb","blau","rot","weiß","grün"]
nationalities = ["Norweger","Ukrainer","Engländer","Spanier","Japaner"]
pets = ["Fuchs","Pferd","Schnecken","Hund","Zebra"]
drink = ["Wasser","Tee","Milch","O-Saft","Kaffee"]
cigarettes = ["Kools", "Chesterfield", "OldGold", "LuckyStrike", "Parliament"]

CSPs = [CSP() for i in range(14)]
houses[1].nationality = "Engländer"
houses[1].color = "blau"
houses[2].color = "weiß"
houses[4].color = "grün"
houses[2].number = 1
houses[4].number = 3

#Der Engländer wohnt im roten Haus.
CSPs[0].needs2Houses = False
CSPs[0].constraints.append(lambda a : (a.color == "rot") == (a.nationality == "Engländer"))

#Der Spanier hat einen Hund.
CSPs[1].needs2Houses=False
CSPs[1].constraints.append(lambda a : (a.pet == "Hund") == (a.nationality == "Spanier"))

#Kaffee wird im grünen Haus getrunken.
CSPs[2].needs2Houses=False
CSPs[2].constraints.append(lambda a : (a.drink == "Kaffee") == (a.color == "grün"))

#Der Ukrainer trinkt Tee.
CSPs[3].needs2Houses=False
CSPs[3].constraints.append(lambda a : (a.drink == "Tee") == (a.nationality == "Ukrainer"))

#Das grüne Haus ist direkt rechts vom weißen Haus.
CSPs[4].needs2Houses = True
CSPs[4].constraints.append(lambda a, b : not ((a.color == "grün") and (b.color == "weiß")) or a.number==None or b.number==None or (a.number - b.number == 1) )

#Der Raucher von Old-Gold-Zigaretten hält Schnecken als Haustiere.
CSPs[5].needs2Houses=False
CSPs[5].constraints.append(lambda a : (a.cigarres == "OldGold") == (a.pet == "Schnecken"))

#Die Zigaretten der Marke Kools werden im gelben Haus geraucht.
CSPs[6].needs2Houses=False
CSPs[6].constraints.append(lambda a : (a.cigarres == "Kools") == (a.color == "gelb"))

#Milch wird im mittleren Haus getrunken.
CSPs[7].needs2Houses=False
CSPs[7].constraints.append(lambda a : a.number == None or ((a.drink == "Milch") == (a.number == 3)))

#Der Norweger wohnt im ersten Haus.
CSPs[8].needs2Houses=False
CSPs[8].constraints.append(lambda a : a.number == None or ((a.nationality == "Norweger") == (a.number == 3)))

#Der Mann, der Chesterfield raucht, wohnt neben dem Mann mit dem Fuchs.
CSPs[9].needs2Houses = True
CSPs[9].constraints.append(lambda a, b : not ((a.cigarres == "Chesterfield") and (b.pet == "Fuchs")) or a.number==None or b.number==None or (abs(a.number - b.number) == 1) )


for houseA in houses:
    for houseB in houses:
        if(CSPs[4].consistent(house1=houseA, house2 = houseB)):
            print("passed")
        else:
            print("not passed")
