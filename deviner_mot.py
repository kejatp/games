import random
import difflib
import tkinter as tk
from tkinter import messagebox

# Lecture du fichier de mots français
with open("./liste_francais/liste_francais.txt", "r") as file:
    french_words_list = [line.strip().lower() for line in file]

class DevinerMotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de deviner le mot")
        self.master.geometry("300x250")

        self.mot_a_deviner = random.choice(french_words_list)
        self.essais = 10

        self.label_mot = tk.Label(master, text="Devinez le mot !")
        self.label_mot.pack()

        self.entry_mot = tk.Entry(master)
        self.entry_mot.pack()

        self.btn_deviner = tk.Button(master, text="Devinez", command=self.deviner)
        self.btn_deviner.pack()

    def deviner(self):
        mot_entre = self.entry_mot.get()
        self.essais -= 1

        similarite = difflib.SequenceMatcher(None, self.mot_a_deviner, mot_entre).ratio()
        messagebox.showinfo("Résultat", f"La similarité entre les deux mots est : {similarite}")

        if mot_entre.lower() == self.mot_a_deviner:
            messagebox.showinfo("Bravo !", "Vous avez deviné le mot correctement.")
            self.master.quit()
        elif self.essais == 0:
            messagebox.showinfo("Désolé !", f"Vous avez utilisé tous vos essais. Le mot était '{self.mot_a_deviner}'.")
            self.master.quit()
        else:
            messagebox.showinfo("Essayez encore !", f"Il vous reste {self.essais} essais.")

def main():
    root = tk.Tk()
    app = DevinerMotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
