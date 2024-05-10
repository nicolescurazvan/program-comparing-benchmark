import json
import random
import os
import sys
import time

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
        out = open(file["name"], "w")
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
        out.write(content)
        out.close()
 
# Run the programs and measure them
def run(config):
    programs = config["programs"]
    inputs = config["inputs"]
    Round = 1
    for file in inputs:
        print("Round " + str(Round) + ": " + file["name"])
        for program in programs:
            cmd = "./" + program + " " + file["name"]
            t = time.time()
            for i in range(0, 5):
                os.system(cmd)
            t = (time.time() - t) / 5
            print("\t" + program + ": " + str(t))
        Round += 1

def main():
    pwd = os.getcwd()
    os.chdir(sys.argv[1])
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
