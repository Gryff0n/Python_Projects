import tkinter as tk
import tkinter.font as tkFont


def caesar_encrypt():
    """
    Cette fonction prend ce qui se trouve dans le widget d'entrée et de clé,
    et encrypte le texte en se servant du code caesar et a l'aide de la clé
    fournie par l'utilisateur; le texte encodé est ensuite inséré dans le 
    widget de sortie. Cette fonction se base sur les unicodes.
    """
    #on récupère le texte original
    plaintext=Entry_box.get(0.0, "end")
    #on récupère la clé
    n=key.get()
    ans = ""
    #si il y a du texte
    if plaintext :
        #si la clé n'est pas numérique on affiche une erreur
        if not n.isnumeric() :
            error.config(text="The key has to be an integer")
        else :
            error.config(text="")
            n=int(n)
            # pour chaque caractère du texte original
            for i in range(len(plaintext)):
                ch = plaintext[i]
                #si le caractère ne possède pas l'unicode correspondant a une lettre minuscule ou majuscule, on le conserve en l'état
                if ord(ch) not in range(65, 91) and ord(ch) not in range(97, 123) :
                    ans+=ch
                # Si c'est une majuscule, on l'encrypte en majuscule
                elif (ch.isupper()):
                    ans += chr((ord(ch) + n-65) % 26 + 65)
                # pareil si c'est une minuscule
                else:
                    ans += chr((ord(ch) + n-97) % 26 + 97)
        #enfin on supprime les potentiels caractères se trouvant dans le widget de sortie et on insert le résultat final
        result.delete(1.0, "end")
        result.insert(1.0, ans)
        return

def caesar_decrypt():
    """
    Cette fonction prend ce qui se trouve dans le widget de sortie et de clé,
    et décrypte le texte en se servant du code caesar et a l'aide de la clé
    fournie par l'utilisateur; le texte décodé est ensuite inséré dans le 
    widget d'entrée'. Cette fonction se base sur les unicodes.
    """
    #on récupère le texte encodé et la clé
    ciphertext = result.get(0.0, "end")
    n = key.get()
    decrypted_text = ""

    #si il y a du texte dans le widget de sortie
    if ciphertext:
        #si la clé n'est pas numérique on affiche une erreur
        if not n.isnumeric():
            error.config(text="The key has to be an integer")
        else:
            error.config(text="")
            n = int(n)
            #pour chaque caractère du texte encodé
            for i in range(len(ciphertext)):
                ch = ciphertext[i]
                #si le caractère ne possède pas un unicode correspondant a une lettre minuscule ou majuscule, on le garde tel quel
                if ord(ch) not in range(65, 91) and ord(ch) not in range(97, 123):
                    decrypted_text += ch
                #si le caractère est majuscule, on le décode en une majuscule
                elif ch.isupper():
                    decrypted_text += chr((ord(ch) - n - 65) % 26 + 65)
                #pareil pour une minuscule
                else:
                    decrypted_text += chr((ord(ch) - n - 97) % 26 + 97)
        #Enfin on supprime les potentiels caractères dans le widget d'entrée et on y insert le texte décodé
        Entry_box.delete(1.0, "end")
        Entry_box.insert(1.0, decrypted_text)
        return

def cipher(event) :
    """
    Cette fonction regarde quel widget de texte possède le focus
    clavier et en déduis si il faut encoder du texte en caesar de 
    l'entrée a la sortie ou si il faut en décoder du caesar de la 
    sortie a l'entrée.
    """
    #si le widget d'entrée possède le focus
    if window.focus_get() == Entry_box :
        #on appelle la fonction de chiffrement
        caesar_encrypt()
    #si le widget de sortie possède le focus
    elif window.focus_get() == result :
        #on appelle la fonction de déchiffrement
        caesar_decrypt()


def translate_to_morse():
    """
    Cette fonction récupère ce qu'il se trouve dans le widget d'entrée
    puis se sert du dictionnaire a sa disposition pour encoder chaque
    caractère en morse puis renvoie le résultat dans le widget de sortie.
    A noter que les espace sont transformés en "/".
    """
    #on définit le dictionnaire dont on va se servir pour encoder
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
        '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
        '@': '.--.-.', ' ': '/'
    }
    #on récupère le texte originel
    text = Entry_box.get(0.0, "end")
    morse_text = []
    #on met chaque caractère en majuscule avant de vérifier leur présence dans le dictionnaire
    for char in text.upper():
        if char in morse_code:
            #si il s'y trouve, on l'ajoute a la liste réponse
            morse_text.append(morse_code[char])
    #une fois fini, on joint la liste en un str
    ans=' '.join(morse_text)
    #on supprime les potentiels caractères déjà présents dans le widget de sortie et on y insert le texte encodé
    result.delete(1.0, "end")
    result.insert(1.0, ans)
    return

def translate_from_morse():
    """
    Cette fonction récupère ce qu'il se trouve dans le widget de sortie
    puis se sert du dictionnaire a sa disposition pour décoder chaque
    caractère depuis du morse puis renvoie le résultat dans le widget d'entrée.
    A noter que les "/" sont transformés en espace.
    """
    morse_code = {
        '.-'   : 'A', '-...' : 'B', '-.-.' : 'C', '-..'  : 'D', '.'    : 'E',
        '..-.' : 'F', '--.'  : 'G', '....' : 'H', '..'   : 'I', '.---' : 'J',
        '-.-'  : 'K', '.-..' : 'L', '--'   : 'M', '-.'   : 'N', '---'  : 'O',
        '.--.' : 'P', '--.-' : 'Q', '.-.'  : 'R', '...'  : 'S', '-'    : 'T',
        '..-'  : 'U', '...-' : 'V', '.--'  : 'W', '-..-' : 'X', '-.--' : 'Y',
        '--..' : 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
        '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
        '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
        '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '/': ' '
    }

    #on récupère le texte en morse
    morse_text = result.get(0.0, "end-1c").split(' ')
    translated_text = []
    #pour chaque combinaison de caractères, on vérifie sa présence dans le dictionnaire
    for code in morse_text:
        if code in morse_code:
            #si il es présent, on le décrypte
            translated_text.append(morse_code[code])
    #enfin on transforme la liste finale en un str
    ans = ''.join(translated_text)
    #on supprime les potentiels caractères déjà présent dans le widget d'entrée puis on y insert le texte décodé
    Entry_box.delete(1.0, "end")
    Entry_box.insert(1.0, ans)
    return


def morse(event) :
    """
    Cette fonction regarde quel widget de texte possède le focus
    clavier et en déduis si il faut encoder du texte en morse de 
    l'entrée a la sortie ou si il faut en décoder du morse de la 
    sortie a l'entrée.
    """
    #si le widget d'entrée possède le focus
    if window.focus_get() == Entry_box :
        #on appelle la fonction de chiffrement
        translate_to_morse()
    #si le widget de sortie possède le focus
    elif window.focus_get() == result :
        #on appelle la fonction de déchiffrement
        translate_from_morse()

def to_vigenere():
    """
    Cette fonction récupère le contenu du widget d'entrée et de clé, puis
    chiffre le texte original avec du code vigenere et la clé fournit par
    l'utilisateur avant d'insérer le résultat final dans le widget de 
    sortie. Cette fonction se base sur les unicodes.
    """
    #on récupère le texte original et la clé
    text = Entry_box.get(0.0, "end-1c")
    vkey = key.get()
    #si la clé n'est pas strictement alphabétique on affiche une erreur
    if not vkey.isalpha() :
        error.config(text="The key has to be a word")
        return
    error.config(text="")
    cip = []
    start = ord('a')
    #si la clé n'est plus assez grande pour le texte, on l'additionne a elle même pour l'allonger
    while len(vkey) < len( text) :
        vkey+=vkey
    #pour chaque caractère du texte et de la clé
    for l, k in zip(text, vkey):
        #si le caractère est un espace on le garde tel quel
        if l == " " :
            cip.append(" ")
        #si le caractère est alphabétique, on l'encode grâce a son unicode et a celui du caractère de la clé
        if l.isalpha() :
            shift = ord(k) - start
            pos = start + (ord(l) - start + shift) % 26
            cip.append(chr(pos))
    #enfin, on joint la liste finale en un str
    ans = ''.join([l for l in cip])
    #on supprime les éventuels caractères déjà présent dans le widget d'arrivée puis on insert le résultat.
    result.delete(0.0, "end")
    result.insert(0.0, ans)
    return

def from_vigenere():
    """
    Cette fonction récupère le contenu du widget de sortie et de clé, puis
    déchiffre le texte encodé avec du code vigenere et la clé fournit par
    l'utilisateur avant d'insérer le résultat final dans le widget d'entrée.
    Cette fonction se base sur les unicodes.
    """
    #on récupère le texte chiffré et la clé
    cipher_text = result.get(0.0, "end-1c")
    vkey = key.get()
    #si la clé n'est pas strictement alphabétique, on affiche une erreur
    if not vkey.isalpha():
        error.config(text="The key has to be a word")
        return
    error.config(text="")
    plain_text = []
    start = ord('a')
    #si la clé n'est pas assez longue pour le texte, on l'additione a elle-même
    while len(vkey) < len(cipher_text) :
        vkey+=vkey
    #pour chaque caractère du texte et de la clé
    for c, k in zip(cipher_text, vkey):
        #si le caractère du texte est un espace, on le garde tel quel
        if c == " " :
            plain_text.append(" ")
        #si le caractère est strictement alphabétique, on le décode grâce a son unicode et celui du caractère de la clé
        if c.isalpha() :
            shift = ord(k) - start
            pos = start + (ord(c) - start - shift) % 26
            plain_text.append(chr(pos))
    #enfin on supprime les éventuels caractères déjà présents dans le widget d'entrée et on y insert le résultat final
    Entry_box.delete(0.0, "end")
    Entry_box.insert(0.0, ''.join(plain_text))
    return

def vigenere(event) :
    """
    Cette fonction regarde quel widget de texte possède le focus
    clavier et en déduis si il faut encoder du texte en vigenere de 
    l'entrée a la sortie ou si il faut en décoder du vigenere de la 
    sortie a l'entrée.
    """
    #si le widget d'entrée possède le focus
    if window.focus_get() == Entry_box :
        #on appelle la fonction de chiffrement
        to_vigenere()
    #si le widget de sortie possède le focus
    elif window.focus_get() == result :
        #on appelle la fonction de déchiffrement
        from_vigenere()

def atbash_cipher():
    """
    Cette fonction récupère le contenu du widget d'entrée,
    l'encode en se servant du code atbash, puis renvoie le 
    résultat dans le widget de sortie. 
    Cette fonction se base sur les unicodes.
    """
    #on récupère le texte original
    text = Entry_box.get(0.0, "end-1c")
    ans = ""
    #pour chaque caractère du texte
    for char in text:
        #si le caractère est strictement alphabétique, on inverse son unicode
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            mirror_index = 25 - index
            mirrored_char = chr(mirror_index + ord('a'))
            #si le caractère est majuscule, on le code en majuscule
            if char.isupper():
                mirrored_char = mirrored_char.upper()
            ans += mirrored_char
        else:
            #si le caractère n'est pas alphabétique, on le garde tel quel
            ans += char
    #enfin on supprime les potentiels caractères déjà présents dans le widget de sortie puis on y insert le résultat final
    result.delete(0.0, "end")
    result.insert(0.0, ans)
    return

def atbash_decipher():
    """
    Cette fonction récupère le contenu du widget de sortie,
    le décode en se servant du code atbash, puis renvoie le 
    résultat dans le widget d'entrée.
    Cette fonction se base sur les unicodes.
    """
    #on récupère le texte chiffré
    text = result.get(0.0, "end-1c")
    ans = ""
    #pour chaque caractère
    for char in text:
        #si il est alphabétique, on inverse son unicode
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            mirror_index = 25 - index
            mirrored_char = chr(mirror_index + ord('a'))
            #si c'est une majuscule, on le remet tel quel
            if char.isupper():
                mirrored_char = mirrored_char.upper()
            ans += mirrored_char
        else:
            #si il n'est pas alphabétique, on le garde tel quel
            ans += char
    #enfin, on supprimes les potentiels caractères déjà présents dans le widget d'entrée et on y insert le résultat décodé
    Entry_box.delete(0.0, "end")
    Entry_box.insert(0.0, ans)
    return

def atbash(event) :
    """
    Cette fonction regarde quel widget de texte possède le focus
    clavier et en déduis si il faut encoder du texte en atbash de 
    l'entrée a la sortie ou si il faut en décoder du atbash de la 
    sortie a l'entrée.
    """
    #si le widget d'entrée possède le focus
    if window.focus_get() == Entry_box :
        #on appelle la fonction de chiffrement
        atbash_cipher()
    #si le widget de sortie possède le focus
    elif window.focus_get() == result :
        #on appelle la fonction de déchiffrement
        atbash_decipher()

#la variable qui stocke quel code est utilisé, caesar par défaut.
ct= cipher

#INTERFACE GRAPHIQUE

#fenêtre principale
window=tk.Tk(className="Sphynx 1.0")
window.geometry("1500x750")
window["background"]="#4f4f4f"
window.resizable(False, False)
window.iconbitmap(default="image/sphynx.ico")
window.title("Sphynx 1.0")

#logo
img = tk.PhotoImage(file="image/sphynx.png")
logo = tk.Label(window, image = img, background="#4f4f4f")
logo.pack()
logo.place(relx=0.502, rely=0.13, anchor="n")

#ornaments
tplefcor = tk.PhotoImage(file="image/corner.png")
tplefcorimg = tk.Label(window, image=tplefcor, background="#4f4f4f")
tplefcorimg.pack()
tplefcorimg.place (relx = 0.0001, rely = 0.001, anchor="nw")

tprigcor = tk.PhotoImage(file="image/corner (1).png")
tprigcorimg = tk.Label(window, image=tprigcor, background="#4f4f4f")
tprigcorimg.pack()
tprigcorimg.place (relx = 0.999, rely = 0.001, anchor="ne")

botlefcor = tk.PhotoImage(file="image/corner (2).png")
botlefcorimg = tk.Label(window, image=botlefcor, background="#4f4f4f")
botlefcorimg.pack()
botlefcorimg.place (relx = 0.0001, rely = 0.999, anchor="sw")

botrigcor = tk.PhotoImage(file="image/corner (3).png")
botrigcorimg = tk.Label(window, image=botrigcor, background="#4f4f4f")
botrigcorimg.pack()
botrigcorimg.place (relx = 0.999, rely = 0.999, anchor="se")

#titre
fontExample = tkFont.Font(family="Arial", size=20, weight="bold", slant="italic")
greeting = tk.Label(text="Welcome to Sphynx\nFor your everyday encrypting needs !", font=("Georgia", 30), background="#4f4f4f", foreground="#9989d6", )
greeting.pack()

#bloc d'entrée
l_enc = tk.Label(text="Encipher", font=fontExample, background="#4f4f4f")
l_enc.pack()
l_enc.place(relx=0.25, rely=0.25, anchor="s")
Entry_box = tk.Text(width=40, height=12, font=('bold',15))
Entry_box.bind('<KeyRelease>', ct)
Entry_box.pack()
Entry_box.place(relx=0.1, rely=0.5, anchor="w")

#bloc de sortie
l_dec = tk.Label(text="Decipher", font=fontExample, background="#4f4f4f")
l_dec.pack()
l_dec.place(relx=0.75, rely=0.25, anchor="s")
result = tk.Text(width=40, height=12, font=('bold',15))
result.bind('<KeyRelease>', ct)
result.pack()
result.place(relx=0.9, rely=0.5, anchor="e")

#desc
desc = tk.Label(text = "The Caesar cipher is one of the earliest known and simplest ciphers.\n It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet.\n For example, with a shift of 1, A would be replaced by B, B would become C, and so on.\n The method is named after Julius Caesar, who apparently used it to communicate with his generals.", font = ("Arial",12, "bold"), background = "#4f4f4f")
desc.pack()
desc.place(relx=0.5, rely=0.81, anchor="s")

#key
l_key = tk.Label(text="Key", font=fontExample, background="#4f4f4f")
l_key.pack()
l_key.place(relx=0.5, rely=0.96, anchor="s")
key= tk.Entry()
key.pack()
key.place(relx=0.5, rely=0.9, anchor="s")

#error
error = tk.Label(font=('Times New Roman bold',20), background="#4f4f4f", foreground="#bf3945")
error.pack()
error.place(relx = 0.5, rely = 0.86, anchor="s")


def cryptool() :
    """
    Cette fonction est appelée quand un des radioboutons pour séléctionner le code a utiliser est préssé.
    elle récupère la valeur de v, c'est a dire la valeur du bouton séléctionné, et agis en conséquence
    pour modifier le code utilisé par le programme.
    """
    #si le premier bouton est pressé
    if v.get() == "1" :
        #le code utilisé est cipher
        ct = cipher
        #on réinitialise le champ d'erreur
        error.config(text="")
        #on affiche la description du code utilisé pour que l'utilisateur sache de quoi il s'agit
        desc.config(text="The Caesar cipher is one of the earliest known and simplest ciphers.\n It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet.\n For example, with a shift of 1, A would be replaced by B, B would become C, and so on.\n The method is named after Julius Caesar, who apparently used it to communicate with his generals.")
        #on affiche le champ pour la clé
        l_key.pack()
        key.pack()
        key.place(relx=0.5, rely=0.9, anchor="s")
        l_key.place(relx=0.5, rely=0.96, anchor="s")
        #on réaffecte les events
        Entry_box.bind('<KeyRelease>', ct)
        result.bind('<KeyRelease>', ct)
    #si le 2e bouton est pressé
    elif v.get() == "2" :
        #le code utilisé est le morse
        ct = morse
        #on affiche la description du morse
        desc.config(text="Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations,\n called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph.")
        #on réinitialise le champ d'erreur
        error.config(text="")
        #on cache le champ de clé
        l_key.pack_forget()
        key.pack_forget()
        key.place_forget()
        l_key.place_forget()
        #on réaffecte les events
        Entry_box.bind('<KeyRelease>', ct)
        result.bind('<KeyRelease>', ct)
    #si le 3e bouton est pressé
    elif v.get() == "3" :
        #le code utilisé est le vigenere
        ct = vigenere
        #on réinitialise le champ d'erreur
        error.config(text="")
        #on affiche la description du vigenere
        desc.config(text="The Vigenère cipher is type of substitution cipher used for data encryption in which the original plaintext structure is\n somewhat concealed in the ciphertext by using several different monoalphabetic substitution ciphers rather than just one;\n the code key specifies which particular substitution is to be employed for encrypting each plaintext symbol. The cipher was invented in 1553 by the Italian\n cryptographer Giovan Battista Bellaso but for centuries was attributed to the 16th-century French cryptographer Blaise de Vigenère, who devised a similar cipher in 1586. ")
        #on affiche le champ de clé
        l_key.pack()
        key.pack()
        key.place(relx=0.5, rely=0.9, anchor="s")
        l_key.place(relx=0.5, rely=0.96, anchor="s")
        #on réaffecte les event
        Entry_box.bind('<KeyRelease>', ct)
        result.bind('<KeyRelease>', ct)
    #si le 4e bouton est pressé
    elif v.get() == "4" :
        #le code utilisé est atbash
        ct = atbash
        #on réinitialise le champ d'erreur
        error.config(text="")
        #on affiche la description de l'atbash
        desc.config(text="The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed.\n I.e. all 'A's are replaced with 'Z's, all 'B's are replaced with 'Y's, and so on. It was originally used for the Hebrew alphabet,\n but can be used for any alphabet.")
        #on cache le champ de clé
        l_key.pack_forget()
        key.pack_forget()
        key.place_forget()
        l_key.place_forget()
        #on réaffecte les events
        Entry_box.bind('<KeyRelease>', ct)
        result.bind('<KeyRelease>', ct)


#valeur du bouton pressé
v = tk.StringVar(window, "1")

#valeurs et noms des boutons, dans l'ordre
values = {"Caesar" : 1,
          "Morse" : 2,
          "Vigenere" : 3,
          "Atbash" : 4}


#création des boutons
for i, (text, value) in enumerate(values.items()):
    button = tk.Radiobutton(window, text=text, variable=v, value=value, indicator=0, background="light blue", font="bold", borderwidth=2, bg="#9989d6")
    button.place(x=692, y=280 + 1.5*i * 40, width=120, height=30)
    button.config(command=cryptool)


#appel de l'interface graphique
window.mainloop()