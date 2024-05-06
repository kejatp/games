import random
import difflib
import tkinter as tk
from tkinter import messagebox

# Assurez-vous d'avoir téléchargé le package 'punkt' de nltk
import nltk
nltk.download('punkt')
nltk.download('words')
from nltk.corpus import words

# Charger le dictionnaire français
mots_francais = words.words()

class DevinerMotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de deviner le mot")
        self.master.geometry("300x200")

        self.mot_a_deviner = random.choice(mots_francais)

        self.label_mot = tk.Label(master, text="Devinez le mot !")
        self.label_mot.pack()

        self.entry_mot = tk.Entry(master)
        self.entry_mot.pack()

        self.btn_deviner = tk.Button(master, text="Devinez", command=self.deviner)
        self.btn_deviner.pack()

    def deviner(self):
        mot_entre = self.entry_mot.get()
        similarite = difflib.SequenceMatcher(None, self.mot_a_deviner, mot_entre).ratio()
        messagebox.showinfo("Résultat", f"La similarité entre les deux mots est : {similarite}")

        if mot_entre.lower() == self.mot_a_deviner.lower():
            messagebox.showinfo("Bravo !", "Vous avez deviné le mot correctement.")
            self.mot_a_deviner = random.choice(mots_francais)
        else:
            messagebox.showinfo("Essayez encore !", "Essayez de deviner un autre mot.")

def main():
    root = tk.Tk()
    app = DevinerMotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()