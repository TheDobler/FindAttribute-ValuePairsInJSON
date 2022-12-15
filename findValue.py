import json
import os

path = "" # The path to the folder with the json files
field = ""
allFiles = []

def printArray(arr):
     #Prints all values of the desired attribute for all files
     if arr == []:
          f.write("Specified name of attribute does not exist\n")
     else: 
          i = 1
          for filed in arr:
               #print('  ' + str(i) + '. ' + filed[0] + ' : ' + str(filed[1]))
               f.write('  ' + str(i) + '. ' + filed[0] + ' : ' + str(filed[1]) + '\n')
               i = i + 1



def readJSON(data, MainObj):
    # Loops through all attributes in the json file and puts the desired attribute and value in an array
     for o in data:
          if type(data[o]) == list:
               #print(o + " is type " + str(type(data[o])))
               MainObj = MainObj + o + '.'
               for obj in data[o]:
                    try:
                         allFiles.append([MainObj + field, obj[field]])
                    except KeyError:
                         if o == field:
                              allFiles.append([MainObj + data[o], obj])
                         continue
               MainObj = ''
          if type(data[o]) == dict:
               #print(o + " is type " + str(type(data[o])))
               MainObj = MainObj + o + '.'
               readJSON(data[o], MainObj)
               MainObj = ''
          if type(data[o]) == tuple:
               # Nothing happens
               print(o + " is type " + str(type(data[o])))
          elif o == field:
               allFiles.append([ MainObj + field, data[o]])
               MainObj = ''
     return allFiles #Returns all the array with all the values in the json file

field = input("Type in the name of an atributtia in the json file: ")
f = open("AtributeValue.txt", "w") # If the file does not exist, a new file is created
i = 0
for subdir, dirs, files in os.walk(path): # Loops through all folders, subfolders and files
    MainObj = ''
    for file in files: # Loops through all the files in the folder
        filepath = subdir + os.sep + file
        if filepath.endswith(".json"): # Finds the file with the json extension
          f.write(file + '\n') # Writes the name of the json file to the text file
          try:
               data = json.loads(open(filepath).read())
          except UnicodeDecodeError:
               f.write(str(UnicodeDecodeError.reason) + '\n')
               continue
          retValue = readJSON(data, MainObj)
          printArray(retValue)
          allFiles = []
          i = i + 1
f.close()
print('Done! Browsing through ' + str(i) + ' json file(s)')