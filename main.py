from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Fifa 21 Potentials')

close1 = Button(root, text="Close", command=root.quit).pack()


def openSquadBuilder():
    squadBuilder = Toplevel()
    squadBuilder.title('Squad Builder')
    def haalandStats_squadBuilder():
        haalandNameSquadBuilder = Label(squadBuilder, text="Erling Haaland").grid(column=33, row=0)
        haalandAgeSquadBuilder = Label(squadBuilder, text="Age=19").grid(column=35, row=0)
        haalandOvrSquadBuilder = Label(squadBuilder, text="OVR=86").grid(column=37, row=0)
        haalandPotSquadBuilder = Label(squadBuilder, text="POT=92").grid(column=33, row=2)
        haalandPriceSquadBuilder = Label(squadBuilder, text="Price=104.5m").grid(column=35, row=2)
    def chooseST():
        haalandChoose = Button(squadBuilder, text="Erling Haaland", command=haalandStats_squadBuilder).grid(column=0, row=0)
    playerSt = Button(squadBuilder, text="ST", pady=20, padx=20, command=chooseST).grid(column=35, row=1)
    playerCam = Button(squadBuilder, text="CAM", pady=20, padx=20, command=chooseCam).grid(column=35, row=3)
    playerLm = Button(squadBuilder, text="LM", pady=20, padx=20, command=chooseLm/Rm/Lw/Rw).grid(column=10, row=3)
    playerRm = Button(squadBuilder, text="RM", pady=20, padx=20, command=chooseLm/Rm/Lw/Rw).grid(column=60, row=3)
    playerCdm1 = Button(squadBuilder, text="CDM", pady=20, padx=20, command=chooseCdm/Cb/Cm/Rb/Lb).grid(column=20, row=6)
    playerCdm2 = Button(squadBuilder, text="CDM", pady=20, padx=20, command=chooseCdm/Cb/Cm/Rb/Lb).grid(column=50, row=6)
    playerCb1 = Button(squadBuilder, text="CB", pady=20, padx=20, command=chooseRb/Cb/Lb/Cdm).grid(column=20, row=8)
    playerCb2 = Button(squadBuilder, text="CB", pady=20, padx=20, command=chooseRb/Cb/Lb/Cdm).grid(column=50, row=8)
    playerLb = Button(squadBuilder, text="LB", pady=20, padx=20, command=chooseRb/Cb/Lb/Cdm/Rwb/Lwb).grid(column=60, row=7)
    playerRb = Button(squadBuilder, text="LB", pady=20, padx=20, command=chooseRb/Cb/Lb/Cdm/Rwb/Lwb).grid(column=10, row=7)
    playerGk = Button(squadBuilder, text="GK", pady=20, padx=20, command=chooseGk).grid(column=35, row=9)

openTeamBuilder = Button(root, text="Open team builder", command=openSquadBuilder).pack()

def Havertz():
    havertz = Toplevel()
    havertz.title('Kai Havertz')
    havertzPot = Label(havertz, text="92", bg="green").grid(column=10, row=0)
    havertzAge = Label(havertz, text="21", bg="green").grid(column=10, row=1)
    havertzPosition = Label(havertz, text="CAM, RM, CM").grid(column=10, row=2)
    havertzOvr = Label(havertz, text="84", bg="green").grid(column=10, row=3)
    age4 = Label(havertz, text="AGE").grid(column=9, row=1)
    pot4 = Label(havertz, text="POT").grid(column=9, row=0)
    position4 = Label(havertz, text="POSITION(S)").grid(column=9, row=2)
    ovr4 = Label(havertz, text="OVR").grid(column=9, row=3)

def Odegaard():
    odegaard = Toplevel()
    odegaard.title('Martin Odegaard')
    odegaardPot = Label(odegaard, text="89", bg="green").grid(column=10, row=0)
    odegaardAge = Label(odegaard, text="21", bg="green").grid(column=10, row=1)
    odegaardPosition = Label(odegaard, text="CAM, CM").grid(column=10, row=2)
    odegaardOvr = Label(odegaard, text="84", bg="green").grid(column=10, row=3)
    pot3 = Label(odegaard, text="POT").grid(column=9, row=0)
    age3 = Label(odegaard, text="AGE").grid(column=9, row=1)
    position3 = Label(odegaard, text="POSITION(S)").grid(column=9, row=2)
    ovr3 = Label(odegaard, text="OVR").grid(column=9, row=3)

def deLigt():
    deligt = Toplevel()
    deligt.title('Matthijs de Ligt')
    deligtPot = Label(deligt, text="92", bg="green").grid(column=10, row=0)
    potl2 = Label(deligt, text="POT").grid(column=9, row=0)
    deligtAge = Label(deligt, text="20", bg="green").grid(column=10, row=1)
    age2 = Label(deligt, text="AGE").grid(column=9, row=1)
    deligtPosition = Label(deligt, text="CB").grid(column=10, row=2)
    position2 = Label(deligt, text="POSITION(S)").grid(column=9, row=2)
    deligtOvr = Label(deligt, text="85", bg="green").grid(column=10, row=3)
    ovr2 = Label(deligt, text="OVR").grid(column=9, row=3)

def Hakimi():
    hakimi = Toplevel()
    hakimi.title('Achraf Hakimi')
    hakimiPot = Label(hakimi, text="88", bg="green").grid(column=10, row=0)
    hakimiAge = Label(hakimi, text="21", bg="green").grid(column=10, row=1)
    hakimiPosition = Label(hakimi, text="RM").grid(column=10, row=2)
    hakimiOvr = Label(hakimi, text="83", bg="green").grid(column=10, row=3)
    ovr6 = Label(hakimi, text="OVR").grid(column=9, row=3)
    age6 = Label(hakimi, text="AGE").grid(column=9, row=1)
    pot6 = Label(hakimi, text="POT").grid(column=9, row=0)
    position6 = Label(hakimi, text="POSITION(S)").grid(column=9, row=2)

def Donnarumma():
    donnarumma = Toplevel()
    donnarumma.title('Gianluigi Donnarumma')
    donnarummaPot = Label(donnarumma, text="92", bg="green").grid(column=10, row=0)
    donnarumaAge = Label(donnarumma, text="21", bg="green").grid(column=10, row=1)
    donnarumaPosition = Label(donnarumma, text="GK").grid(column=10, row=2)
    donnarumaOvr = Label(donnarumma, text="86", bg="green").grid(column=10, row=3)
    ovr5 = Label(donnarumma, text="OVR").grid(column=9, row=3)
    age5 = Label(donnarumma, text="AGE").grid(column=9, row=1)
    pot5= Label(donnarumma, text="POT").grid(column=9, row=0)
    position5 = Label(donnarumma, text="POSITION(S)").grid(column=9, row=2)

def Valverde():
    valverde = Toplevel()
    valverde.title('Federico Valverde')
    valverdePot = Label(valverde, text="89", bg="green").grid(column=10, row=0)
    valverdeAge = Label(valverde, text="19", bg="green").grid(column=10, row=1)
    valverdePosition = Label(valverde, text="CM, CDM").grid(column=10, row=2)
    valverdeOvr = Label(valverde, text="83", bg="green").grid(column=10, row=3)
    ovr7 = Label(valverde, text="OVR").grid(column=9, row=3)
    age7 = Label(valverde, text="AGE").grid(column=9, row=1)
    pot7 = Label(valverde, text="POT").grid(column=9, row=0)
    position7 = Label(valverde, text="POSITION(S)").grid(column=9, row=2)

def Felix():
    felix = Toplevel()
    felix.title('Joao Felix Sequeira')
    felixPot = Label(felix, text="93", bg="green").grid(column=10, row=0)
    felixAge = Label(felix, text="20", bg="green").grid(column=10, row=1)
    felixPosition = Label(felix, text="CF, ST").grid(column=10, row=2)
    felixOvr = Label(felix, text="83", bg="green").grid(column=10, row=3)
    ovr8 = Label(felix, text="OVR").grid(column=9, row=3)
    age8 = Label(felix, text="AGE").grid(column=9, row=1)
    pot8 = Label(felix, text="POT").grid(column=9, row=0)
    position8 = Label(felix, text="POSITION(S)").grid(column=9, row=2)

def Upamecano():
    upamecano = Toplevel()
    upamecano.title('Dayot Upamecano')
    upamecanoPot = Label(upamecano, text="90", bg="green").grid(column=10, row=0)
    upamecanoAge = Label(upamecano, text="21", bg="green").grid(column=10, row=1)
    upamecanoPosition = Label(upamecano, text="CB").grid(column=10, row=2)
    upamecanoOvr = Label(upamecano, text="81", bg="green").grid(column=10, row=3)
    ovr9 = Label(upamecano, text="OVR").grid(column=9, row=3)
    age9 = Label(upamecano, text="AGE").grid(column=9, row=1)
    pot9 = Label(upamecano, text="POT").grid(column=9, row=0)
    position9 = Label(upamecano, text="POSITION(S)").grid(column=9, row=2)

def Haaland():
    haaland = Toplevel()
    haaland.title('Erling Haaland')
    haalandPot = Label(haaland, text="92", bg="green").grid(column=10, row=0)
    haalandAge = Label(haaland, text="19", bg="green").grid(column=10, row=1)
    haalandPosition = Label(haaland, text="ST").grid(column=10, row=2)
    haalandOvr = Label(haaland, text="86", bg="green").grid(column=10, row=3)
    ovr = Label(haaland, text="OVR").grid(column=9, row=3)
    age = Label(haaland, text="AGE").grid(column=9, row=1)
    pot = Label(haaland, text="POT").grid(column=9, row=0)
    position = Label(haaland, text="POSITION(S)").grid(column=9, row=2)

def Sancho():
    sancho = Toplevel()
    sancho.title('Jadon Sancho')
    sanchoPot = Label(sancho, text="92", bg="green").grid(column=10, row=0)
    pot1 = Label(sancho, text="POT").grid(column=9, row=0)
    sanchoAge = Label(sancho, text="20", bg="green").grid(column=10, row=1)
    age1 = Label(sancho, text="AGE").grid(column=9, row=1)
    sanchoPosition = Label(sancho, text="RM, CF, CAM").grid(column=10, row=2)
    position1 = Label(sancho, text="POSITION(S)").grid(column=9, row=2)
    sanchoOvr = Label(sancho, text="86", bg="green").grid(column=10, row=3)
    ovr1 = Label(sancho, text="OVR").grid(column=9, row=3)


def open():
    top = Toplevel()
    top.title('88+ potential under 21 years old(expensive)')
    haalandLink = Button(top, text="Erling Haaland", fg="blue", command=Haaland).grid(column=5, row=0)
    sanchoLink = Button(top, text="Jadon Sancho", fg="blue", command=Sancho).grid(column=5, row=1)
    deLigtLink = Button(top, text="Matthijs de Ligt", fg="blue", command=deLigt).grid(column=5, row=2)
    odegaardLink = Button(top, text="Martin Odegaard", fg="blue", command=Odegaard).grid(column=5, row=3)
    havertzLink = Button(top, text="Kai Havertz", fg="blue", command=Havertz).grid(column=5, row=4)
    donnarummaLink = Button(top, text="Gianluigi Donnarumma", fg="blue", command=Donnarumma).grid(column=5, row=5)
    hakimiLink = Button(top, text="Achraf Hakimi", fg="blue", command=Hakimi).grid(column=5, row=6)
    valverdeLink = Button(top, text="Federico Valverde", fg="blue", command=Valverde).grid(column=5, row=7)
    felixLink = Button(top, text="Joao Felix Sequeira", fg="blue", command=Felix).grid(column=5, row=8)
    upamecanoLink = Button(top, text="Dayot Upamecano", fg="blue", command=Upamecano)


btn = Button(root, text="88+ potential under 21 years old(expensive)", command=open).pack()












root.mainloop()
