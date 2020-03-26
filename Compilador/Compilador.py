# -*- coding: utf-8 -*-
import json


dictionaryFile = open("instrucciones.json", 'r') 
dictionary = json.load(dictionaryFile)

instructionsFile = open("Ejemplo1.txt", 'r')
instruction = instructionsFile.readlines()
instructions = []

for i in range(len(instruction)):
    instruction[i] = instruction[i].replace(",", "")
    instruction[i] = instruction[i].replace("\n", "")
    instructions.append(instruction[i].split(" "))

binary = []
for i in range(len(instructions)):
    instruc = dictionary[instructions[i][0]]
    operand1 = instructions[i][1]
    operand2 = instructions[i][2]
    if len(instructions[i][1]) > 0:
        if instructions[i][1][0] == "R":
            operand1 = operand1.replace("R", "")
            operand1 = int(operand1)
            operand1 = "{0:b}".format(operand1)
            instruc = instruc + "10"
        
        elif instructions[i][1].isdigit() :
            operand1 = int(instructions[i][1])
            operand1 = "{0:b}".format(operand1)
            instruc = instruc + "00"
        
        if len(operand1) < 8:
                for j in range(8 - len(operand1)):
                    operand1 = "0" + operand1
       
    if len(instructions[i][2]) > 0:
        if instructions[i][2][0] == "[" and instructions[i][2][len(instructions[i][2]) - 1] == "]":
            operand2 = operand2.replace("[", "")
            operand2 = operand2.replace("]", "")
            instruc = instruc + "1"
        
        elif instructions[i][2][0] == "R":
            operand2 = operand2.replace("R", "")
            operand2 = int(operand2)
            operand2 = "{0:b}".format(operand2)
            instruc = instruc + "0"
        
        if len(operand2) < 8:
            for j in range(8 - len(operand2)):
                operand2 = "0" + operand2
                
    for j in range(8 - len(instruc)):
        instruc = instruc + "0"
    
    binary.append(instruc + " " + operand1 + " " + operand2)
    
print(binary)

print(instructions)
print(instructions[1])
print(type (instructions[1][1]))