#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish

import tkinter as tk
from tkinter import messagebox

import json

light = 3
people = 4

def show_popup(setter):
    def submit():
        selected_option = var.get()
        if selected_option == "True":
            # messagebox.showinfo("Resposta", "Você escolheu: Sim")
            if setter == 3:
                return_value.append(True)
            elif setter == 4:
                return_value.append(True)
        elif selected_option == "False":
            # messagebox.showinfo("Resposta", "Você escolheu: Não")
            if setter == 3:
                return_value.append(False)
            elif setter == 4:
                return_value.append(False)
        else:
            messagebox.showwarning("Aviso", "Nenhuma opção selecionada")
            show_popup(setter)
            popup.destroy()
        popup.destroy()  # Fecha o popup

    popup = tk.Tk()
    popup.title("Escolha uma opção")

    var = tk.StringVar(value="")

    title = "";
    if setter == 3:
        title = "A luz da sala está acessa?"
    elif setter == 4:
        title = "Tem alguém dentro da sala?"
    
    tk.Label(popup, text=title).pack(pady=10)
    tk.Radiobutton(popup, text="Sim", variable=var, value="True").pack(anchor="w")
    tk.Radiobutton(popup, text="Não", variable=var, value="False").pack(anchor="w")

    tk.Button(popup, text="Confirmar", command=submit).pack(pady=10)

    return_value = []

    popup.mainloop()
    
    return return_value[0]

while 0 == 0:
    lightRes = show_popup(light)
    peopleRes = show_popup(people)

    data = {'light': lightRes, 'people': peopleRes}

    msgs = [{'topic': "info", 'payload': json.dumps(data)}]

    host = "18.234.70.138"

    if __name__ == '__main__':
        publish.multiple(msgs, hostname=host)