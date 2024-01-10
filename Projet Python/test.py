import time as sleep
import simpleaudio as sa
import numpy as np
import turtle as tr

FICHIER = "partitions.txt"

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

def read_sheet(num):
    c = 0
    cpt = 0
    file = open(FICHIER, "r")
    lignes = file.readlines()
    for i in lignes:
        cpt += 1
        if cpt == num:
            c = i

    space = True
    every_note = []
    temp=""
    for z in range(len(c)):
        elem = c[z]
        if elem != " " and elem !="\n":
            if space == True:
                temp = elem
            else:
                temp = temp+elem
            space = False
        else:
            space = True
            every_note.append(temp)


    freq = []
    fig = []

    for note in every_note :

        # FREQUENCE
        freq2 = 0
        if "DO" in note:
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
        if 'c' in note:
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

    finaly = []
    finaly.append(every_note)
    finaly.append(freq)
    finaly.append(fig)
    file.close()
    return finaly

def sound(freq,duration) : # la fonction sound qui permet d'émettre un son à partir d'une frequence et d'un temps
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

#INTERFACE GRAPHIQUE PAR TKINTER (non fini).

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