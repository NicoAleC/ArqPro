# -*- coding: utf-8 -*-
import json


dictionaryFile = open("instrucciones.json", 'r') 
dictionary = json.load(dictionaryFile)

instructionsFile = open("Ejemplo.txt", 'r')
instruction = instructionsFile.readlines()
instructions = []

for i in range(len(instruction)):
    instruction[i] = instruction[i].replace(",", "")
    instruction[i] = instruction[i].replace("\n", "")
    instructions.append(instruction[i].split(" "))

print(instructions)
print(instructions[1])
aux = "{0:b}".format(5)
print(aux)

if len(aux) < 8:
    for i in range(8 - len(aux)):
        aux = "0" + aux

print(aux)
print(type (instructions[1][1]))