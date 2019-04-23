
def readfiles(filename):
    fps = "experiments/AlgorithmTesting/"
    fpe = "/results.txt"
    filepath = fps + filename + fpe
    fileread = open(filepath,"r")
    fileoutput = fileread.read()
    fileread.close()
    return fileoutput

############################################
##                Output File             ##
############################################

out = open("output.txt","a")

############################################
##                Input File              ##
############################################
AE = readfiles("ApproximateEntropy")
NOT = readfiles("NonOverlappingTemplate")
FQ = readfiles("Frequency")
LC = readfiles("LinearComplexity")
BFQ = readfiles("BlockFrequency")
OLT = readfiles("OverlappingTemplate")
RANK = readfiles("Rank")
UNI = readfiles("Universal")
SERI = readfiles("Serial")
RUNS = readfiles("Runs")
REV = readfiles("RandomExcursionsVariant")
RE = readfiles("RandomExcursions")
FFT = readfiles("FFT")
CS = readfiles("CumulativeSums")
LR = readfiles("LongestRun")

out.write("Approximate Entropy:\n")
out.write(AE)
out.write("\n\n")
out.write("NonOverlapping Template:\n")
out.write(NOT)
out.write("\n\n")
out.write("Frequency:\n")
out.write(FQ)
out.write("\n\n")
out.write("Linear Complexity:\n")
out.write(LC)
out.write("\n\n")
out.write("Block Frequency:\n")
out.write(BFQ)
out.write("\n\n")
out.write("Overlapping Template:\n")
out.write(OLT)
out.write("\n\n")
out.write("Rank:\n")
out.write(RANK)
out.write("\n\n")
out.write("Universal:\n")
out.write(UNI)
out.write("\n\n")
out.write("Serial:\n")
out.write(SERI)
out.write("\n\n")
out.write("Runs:\n")
out.write(RUNS)
out.write("\n\n")
out.write("Random Excursions Variant:\n")
out.write(REV)
out.write("\n\n")
out.write("Random Excursions:\n")
out.write(RE)
out.write("\n\n")
out.write("FFT:\n")
out.write(FFT)
out.write("\n\n")
out.write("Cumulative Sumation:\n")
out.write(CS)
out.write("\n\n")
out.write("Longest Run:\n")
out.write(LR)
out.write("\n\n")