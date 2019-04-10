import sys,os
path = os.getcwd()
testout = os.path.join(path + "/experiments/AlgorithmTesting")
dirlist = os.listdir(testout)
fout = open("testoutdir", "a+")
for x in dirlist:
    fout.write("\"" + x + "\"\n")
fout.close()
