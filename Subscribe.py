#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho

from tkinter import messagebox

import json

def on_message(mosq, obj, msg):
    # print("{:<20} {} {}".format(msg.topic, msg.qos, msg.payload.decode('utf-8')))
    
    if msg.topic == "info":
        res = msg.payload.decode('utf-8')
        objRes = json.loads(res)
        if objRes['light'] == False and objRes['people'] == True:
            messagebox.showwarning("Aviso", "Acendendo a luz!")
            
        if objRes['light'] == True and objRes['people'] == True:
            messagebox.showwarning("Aviso", "Acendendo a luz!")
            
        if objRes['light'] == True and objRes['people'] == False:
            messagebox.showwarning("Aviso", "Apagando a luz!")
            
        if objRes['light'] == False and objRes['people'] == False:
            messagebox.showwarning("Aviso", "Apagando a luz!")

# def on_publish(mosq, obj, mid):
    # pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    # client.on_publish = on_publish

    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("3.91.103.79", 1883)

    client.subscribe("info", 0)

    while client.loop() == 0:
        pass

# vi: set fileencoding=utf-8 :