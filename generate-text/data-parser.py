import csv

# subdirectory for text
genDir = "resource"

# open csv 
with open('../data/20-sample.csv', 'r') as csvSampleFile, open(genDir+"/inspiration.txt", 'w') as inspirationFile, open(genDir+"/does.txt", 'w') as whatItDoesFile, open(genDir+"/built.txt", 'w') as builtFile, open(genDir+"/challenges.txt", 'w') as challengesFile, open(genDir+"/accomplishments.txt", 'w') as accomplishmentsFile, open(genDir+"/learned.txt", 'w') as learnedFile, open(genDir+"/next.txt", 'w') as nextFile:
    reader = csv.reader(csvSampleFile)
    # iterate through
    for row in reader:
        # get the row's data
        doc = eval(row[2]) 
        # parse to individual files
        inspirationFile.write(doc[0]+ " ")
        whatItDoesFile.write(doc[1]+ " ")
        builtFile.write(doc[2]+ " ")
        challengesFile.write(doc[3]+ " ")
        accomplishmentsFile.write(doc[4]+ " ")
        learnedFile.write(doc[5]+ " ")
        nextFile.write(doc[6]+ " ")
