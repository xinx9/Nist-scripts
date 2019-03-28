def readfiles(filename):
    fps = "experiments/AlgorithmTesting/"
    fpe = "/results.txt"
    filepath = fps + filename + fpe
    fileread = open(filepath,"r")
    return fileread.read()

############################################
##                Output File             ##
############################################

out = open("TestData.txt","a")

############################################
##                Input File              ##
############################################
strout = ""
aproxent = readfiles("ApproximateEntropy")
blkfreq = readfiles("BlockFrequency")

out.write(aproxent)
out.write("\n")
out.write(blkfreq)
out.write("\n\n")