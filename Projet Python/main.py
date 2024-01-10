import time as sleep
import numpy as np
import simpleaudio as sa
import turtle as tr


FICHIER="partitions.txt"

#dictionnaire pour les notes.

def Diconote(note,n): #On défini la fonction.
    Nnote = {} #Nnote est notre dictionnaire.
    for i in range(len(note)): #boucle qui parcoure la longueur de liste de note.
        for j in range(len(n)): #boucle qui parcoure la longueur de la liste de nombre.
            if i==j: #condition d'égalité des occurences.
                Nnote[note[i]] = n[j] #ce que prend le dictionnaire.
    return Nnote #retourne le dictionnaire Nnote au programme.

note = ["Do", "Ré", "Mi", "Fa", "Sol", "La", "Si"] # liste de note préranger avec la liste des nombres n par leurs occurences.
n=[1,2,3,4,5,6,7]
print(Diconote(note,n)) #apelle la fonction Diconote.

#dictionnaire pour les fréquence.

def calc_frequency(note, frequences): #On defini la fonction.
    Fnote = {} #Fnote est notre dictionnaire.
    for i in range(len(note)): #Boucle qui parcoure la longueur de la liste de note.
        for j in range(len(frequences)): #Boucle qui parcoure la longueur de la liste de fréquence.
            if i==j:#condition d'égalité des occurences.
                Fnote[note[i]] = frequences[j] #ce que prend le dictionnaire.
    return Fnote #retourne le dictionnaire Fnote au programme.

note = ["Do", "Ré", "Mi", "Fa", "Sol", "La", "Si"] #liste de note préranger avec la liste des fréquence par leurs occurences.
frequences = [264, 297, 330, 352, 396, 440, 495]
print(calc_frequency(note, frequences)) #apelle à la fonction calc_frequency.

#dictionnaire pour les durées.

def calc_duration(figures,d0): #on définie la fonction.
    Fd0={} #Fd0 et notre dictionnaire.
    for i in range(len(figures)): #Boucle qui parcoure la longueur de la liste des figures.
        for j in range(len(d0)): #Boucle qui parcoure la longueur de la liste des durées.
            if i==j: #Condition d'égalité des occurences.
                Fd0[figures[i]]=d0[j] #ce que prend le dictionnaire.
    return Fd0 #retourne le dictionaire Fd0 au programme.
figures=["ronde","blanche","noir","croche"] #liste des figure prérangé avec la liste des duré par leur occurence.
d0=[1000,500,250,125]
print(calc_duration(figures,d0)) #apelle à la fonction calc_duration.

#les durées.
#1 ronde=8 croche = 8*125ms
#2 Blanche= 4 croche= 4*125ms
#3 Noir=2Croche= 2*125ms
#4 Croche= 1croche=125ms
#figure=["ronde","blanche","noir","croche"]
#d0=[1000,500,250,125]
#Fd0={"ronde":1000,"blanche":500,"noir":250,"Croche":125}

#ouvrire le fichier.

def read_line(fichier,num): #on defini la fonction.
    c=0 #variable c qui prend la ligne.
    cpt=0 #compteur cpt qui compte les lignes.
    file=open(fichier,"r") #permet ouvrire le fichier.
    lignes=file.readlines() #lire les lignes du fichier.
    for i in lignes: #boucle qui parcoure les lignes.
        cpt+=1 #compteur qui prend le nombre de ligne.
        if cpt==num: #condition qui permet de prendre la ligne demandé.
            c=i #prend la ligne demandé.
    return c #retourne la ligne demandé c au programme.
fichier=input("saisir votre fichier") #saisir un fichier de type caractére.
num=int(input("saisir une ligne")) #saisir un numéro de ligne.
print(read_line("partitions.txt",num)) #apelle à la fonction read_line.

#lire la ligne du fichier et classé les notes,fréquence et durée dans une liste.

def read_sheet(num):
    c = 0
    cpt = 0
    file = open(FICHIER, "r")


    lignes = file.readlines()      #utilisation de la fonction read_line.
    for i in lignes:
        cpt += 1
        if cpt == num:
            c = i

    space = True #verification.
    every_note = [] #stockage dans une liste.
    temp="" #pour que ce soit  une chaine de caractère.
    for z in range(len(c)): #boucle qui parcoure la longueur de la ligne choisie.
        elem = c[z]
        if elem != " " and elem !="\n": #condition qui demande que l'élément soit à l'intérieur de la chaine de caractére.
            if space == True : #condition booléene.
                temp = elem
            else:
                temp = temp+elem
            space = False
        else:
            space = True
            every_note.append(temp)


    freq = [] #liste de stockage des fréquences.
    fig = [] #liste de sotackage des figures.

    for note in every_note : #boucle qui prend note dans toute les notes de de la ligne.

        # FREQUENCE
        freq2 = 0
        if "DO" in note: #condition des fréquence des notes dans la ligne.
            freq2 = 264
        elif "RE" in note:
            freq2 = 297
        elif "MI" in note:
            freq2 = 330
        elif "FA" in note:
            freq2 = 352
        elif "SOL" in note:
            freq2 = 396
        elif "LA" in note:
            freq2 = 440
        elif "SI" in note:
            freq2 = 495
        elif "Z" in note:
            freq2 = -1
        if freq2 != 0:
            freq.append(freq2)

        # FIGURE
        fig2 = 0
        if 'c' in note: #condition des figures des notes dans la liste.
            fig2 = 125.0
        elif 'n' in note:
            fig2 = 125*2.0
        elif 'b' in note:
            fig2 = 125*4.0
        elif 'r' in note:
            fig2 = 125*8.0
        elif 'p' == note:
            fig[-1] += (fig[-1])/2

        if 'Z' in note:
            fig2 = -fig2

        if fig2 !=0:
            fig.append(fig2)

    finaly = [] #liste qui prend toute les listes.
    finaly.append(every_note) #.append permet d'ajouter les élément a finaly.
    finaly.append(freq)
    finaly.append(fig)
    file.close()
    return finaly #retourne la liste finaly au programme.

num=int(input("saisir une ligne")) #saisir un numéro de ligne.
print("voici: (notes,frequence, durée")
print(read_sheet(num)) #apelle la fonction read_sheet

#definir le son

def sound (freq,duration) : # la fonction sound qui permet d'émettre un son à partir d'une frequence et d'un temps
    sample_rate = 44100
    t = (np.linspace(0.0, duration, num=int(duration*sample_rate), endpoint=False))
    tone = np.sin(freq*t*(6)*np.pi)
    tone *= 8388607/np.max(np.abs(tone))
    tone = tone.astype(np.int32)
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array.append(b)
        i += 1
    audio = bytearray(byte_array)
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    play_obj.wait_done()

#lire la musique avec le son.

def play_sheet(num):
    c = read_sheet(num) #c est la variable qui va prendre notre fonction read_sheet.
    freq = c[1] #freq vas prendre le 1er élément comme fréquence.
    fig = c[2] #fig vas prendre le second élément comme figure.
    for i in range(len(freq)): #boucle qui parcoure la longeur de la frequence.
        frequency = freq[i]
        duration = fig[i]
        if duration < 0 and frequency == -1: #condition qui permet établire le silence.
            sleep.sleep((-duration)/1000)
        else: #sinon si ce n'est pas un silence alors ont prend la note.
            sound(frequency, duration/1000)

print(read_sheet(2))

#sound(396, 0.1875)
play_sheet(24) #commande qui permet de choisir la ligne a jouer.

#Animation pour accompagné la musique

def graph(num):
    c = read_sheet(num) #variable qui prend la fonction read_sheet(num).
    print(c) #afficher c.
    freq = c[1] #freq prend la premier occurence de c.
    fig = c[2] #fig prend la 2eme occurence de c.
    d = 0 #d est initialisé à 0.
    tr.bgcolor("black") #couleur de l'arrière plan.
    colors = ["red", "purple", "blue", "green", "orange", "yellow"] #couleur du motif.
    x = 0 #x est initialisé à 0.
    tr.speed(0) #vitesse du motif.
    for i in range(len(freq)): #boucle qui parcoure la longueur de freq.
        frequency = freq[i] #frequency prend la valeur de freq[i].
        duration = fig[i] #duration prend la valeur de fig[i].
        if duration < 0 or frequency == -1: #condition sur la durée et la frequence.
            if duration < 0: #condition sur la durée.
                sleep.sleep((-1*duration)/1000) #appel au package time.
            else:
                sleep.sleep(duration/1000)#appel au package time.
        else:
            sound(frequency, duration/1000) #appel au package simpleaudio.
            d += 1 #d prend d+1.
            tr.up() #position du motf.
            tr.color(colors[x % 6]) #position du motif.
            tr.width(x / 100 + 1) #position du motif.
            tr.down() #position du motif.
            tr.forward(x*5)#position du motif.
            tr.left(59)#position du motif.
            x = (x + 1) % 360#position du motif.
    tr.exitonclick()#clicker sur le motif pour stoper.

graph(2) #changer la valeur de graph pour changer de partition.




#INTERFACE GRAPHIQUE PAR TKINTER

from tkinter import*
window = Tk()
window.title("Music App")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("3378993_87aa7.ico")
window.config(background='#727170')

# frame pour centré les textes.

frame = Frame(window, bg='#727170')

# ajouter un  Principal texte
label_title = Label(window, text="Welcome on Music app", font=("Helvetica", 40), bg='#727170', fg='black')
label_title.pack()  # permet de mettre au millieu le texte meme en modifient la fenetre.

# ajouter un texte secondaire
label_subtitle = Label(window, text="click to start", font=("Helvetica", 25), bg='#727170', fg='black')
label_subtitle.pack()

# ajoute de bouton

play_button = Button(frame, text="start the music", font=("Helvetica", 25), bg='white', fg='#727170')
play_button.pack()
frame.pack(expand=YES)

window.mainloop()