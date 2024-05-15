import json
import random
import os
import sys
import time
import re

# Create the json file with user input
def getUserInput():
    fin = open("config.json", "r")
    config = json.loads(fin.read())
    for file in config["inputs"]:
        os.remove(file["name"])
    fin.close()

    config = dict()
    programs = input("What programs are you comparing? ").split()
    config["programs"] = programs
    programType = input("What type of input do your programs take? ").strip()
    config["type"] = programType
    inputs = []
    inputsSize = int(input("How many files are you going to generate? "))
    for i in range(0, inputsSize):
        file = dict()
        name = input("What's the name of the file? ").strip()
        file["name"] = name
        if programType in ["matrix<int>", "matrix<float>"]:
            min_rows, max_rows = map(int, input("How many rows does the matrix have? ").split())
            file["min_rows"] = min_rows
            file["max_rows"] = max_rows
            min_cols, max_cols = map(int, input("How many columns does the matrix have? ").split())
            file["min_cols"] = min_cols
            file["max_cols"] = max_cols
            Min, Max = map(int, input("How big are the numbers? ").split())
            file["min"] = Min
            file["max"] = Max 
        elif programType in ["vector<int>", "vector<float>", "vector<string>"]:
            min_len, max_len = map(int, input("How big is the vector? ").split())
            file["min_length"] = min_len
            file["max_length"] = max_len
            if programType == "vector<string>":
                Min, Max = map(int, input("How big are the strings? ").split())
                file["min"] = Min
                file["max"] = Max 
            else:
                Min, Max = map(int, input("How big are the numbers? ").split())
                file["min"] = Min
                file["max"] = Max 
        elif programType in ["int", "float", "string"]:
            if programType == "string":
                Min, Max = map(int, input("How big are the strings? ").split())
                file["min"] = Min
                file["max"] = Max 
            else:
                Min, Max = map(int, input("How big are the numbers? ").split())
                file["min"] = Min
                file["max"] = Max
        else:
            print("Error! Wrong type")
            return
        inputs.append(file)
    
    config["inputs"] = inputs
    return config


# Parse the json file
def getInfo():
    f = open("config.json", "r")
    config = json.loads(f.read())
    f.close()
    return config

def Int(file):
    return str(random.randint(file["min"], file["max"])) + " "

def Float(file):
    return str(random.uniform(file["min"], file["max"])) + " "

def String(file):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "`~!@#$%^&*()-_=+[]{}|\\\"\'<>,.?/"
    chars = lowercase + uppercase + numbers + symbols + " "
    size = random.randint(file["min"], file["max"])
    return "".join(random.choices(chars, k=size)) + "\n"

def Vector(func, file):
    n = random.randint(file["min_length"], file["max_length"])
    content = str(n) + "\n"
    for i in range(0, n):
        content += func(file)
    return content

def Matrix(func, file):
    m = random.randint(file["min_rows"], file["max_rows"])
    n = random.randint(file["min_cols"], file["max_cols"])
    content = str(m) + " " + str(n) + "\n"
    for i in range(0, m):
        for j in range(0, n):
            content += func(file)
        content += "\n"
    return content

# Generate the files
def generate(inputs, filetype):
    for file in inputs:
        fout = open(file["name"], "w")
        content = ""
        if filetype == "int":
            content = Int(file)
        elif filetype == "float":
            content = Float(file)
        elif filetype == "string":
            content = String(file)
        elif filetype == "vector<int>":
            content = Vector(Int, file)
        elif filetype == "vector<float>":
            content = Vector(Float, file)
        elif filetype == "vector<string>":
            content = Vector(String, file)
        elif filetype == "matrix<int>":
            content = Matrix(Int, file)
        elif filetype == "matrix<float>":
            content == Matrix(Float, file)
        else:
            print("Error")
        fout.write(content)
        fout.close()

# Run the programs and measure them
def run(config):
    programs = config["programs"]
    inputs = config["inputs"]
    Round = 1
    for file in inputs:
        print(f"Round {Round}: {file["name"]}")
        for program in programs:
            cmd = f"./{program} {file["name"]}"
            t = time.time()
            for i in range(0, 5):
                os.system(cmd)
            t = (time.time() - t) / 5
            print("\t" + program + ": " + str(t))
        Round += 1

def main():
    if len(sys.argv) != 3:
        print("Error! Wrong number of arguments")
        return
    elif re.match("-i?g?b?r?c?", sys.argv[2]) == None:
        print("Error! Wrong combination of flags")
        return
    
    pwd = os.getcwd()
    os.chdir(sys.argv[1])
    if 'i' in sys.argv[2]:
        config = getUserInput()
        fout = open("config.json", "w")
        fout.write(json.dumps(config, indent=4))
        fout.close()
    else:
        config = getInfo()
    if 'g' in sys.argv[2]:
        generate(config["inputs"], config["type"])
    if 'b' in sys.argv[2]:
        os.system("make build")
    if 'r' in sys.argv[2]:
        run(config)
    if 'c' in sys.argv[2]:
        os.system("make clean")
    os.chdir(pwd)

if __name__ == "__main__":
    main()
