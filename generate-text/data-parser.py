import csv

# subdirectory for text
genDir = "resource"
dataDir = "../data/50-100.csv"

# open csv 
with open(dataDir, 'r') as csvSampleFile, open(genDir+"/inspiration.txt", 'w') as inspirationFile, open(genDir+"/does.txt", 'w') as whatItDoesFile, open(genDir+"/built.txt", 'w') as builtFile, open(genDir+"/challenges.txt", 'w') as challengesFile, open(genDir+"/accomplishments.txt", 'w') as accomplishmentsFile, open(genDir+"/learned.txt", 'w') as learnedFile, open(genDir+"/next.txt", 'w') as nextFile, open(genDir+"/titles.txt", 'w') as titleFile, open(genDir+"/subtitles.txt", 'w') as subTitleFile:
    reader = csv.reader(csvSampleFile)
    next(reader)
    # iterate through
    for row in reader:
        # get the row's data
        doc = eval(row[2]) 
        # parse to individual files
        inspirationFile.write(doc[1]+ "\n ")
        whatItDoesFile.write(doc[2]+ "\n ")
        builtFile.write(doc[3]+ "\n ")
        challengesFile.write(doc[4]+ "\n ")
        accomplishmentsFile.write(doc[5]+ "\n ")
        learnedFile.write(doc[6]+ "\n ")
        nextFile.write(doc[7]+ "\n ")
        # get the title of the project
        title = row[0]
        titleFile.write(title+ "\n")
        # get the subtitle
        subtitle = row[1]
        subTitleFile.write(subtitle+ "\n")
