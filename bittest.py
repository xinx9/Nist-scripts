
def readfiles(filename):
    fps = "experiments/AlgorithmTesting/"
    fpe = "/results.txt"
    filepath = fps + filename + fpe
    fileread = open(filepath,"r")
    fileoutput = file.read()
    fileread.close()
    return fileoutput

############################################
##                Output File             ##
############################################

out = open("dataOutput.txt","a")

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


out.write(AE)
out.write("\n\n")
out.write(NOT)
out.write("\n\n")
out.write(FQ)
out.write("\n\n")
out.write(LC)
out.write("\n\n")
out.write(BFQ)
out.write("\n\n")
out.write(OLT)
out.write("\n\n")
out.write(RANK)
out.write("\n\n")
out.write(UNI)
out.write("\n\n")
out.write(RANK)
out.write("\n\n")
out.write(UNI)
out.write("\n\n")
out.write(SERI)
out.write("\n\n")
out.write(RUNS)
out.write("\n\n")
out.write(REV)
out.write("\n\n")
out.write(RE)
out.write("\n\n")
out.write(FFT)
out.write("\n\n")
out.write(CS)
out.write("\n\n")
out.write(LR)
out.write("\n\n")