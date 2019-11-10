from textgenrnn import textgenrnn

outDir = "outputs"
inDir = "resource"

def generate_text(fileInput, fileOutput):
    textgen = textgenrnn()
    # train the model
    textgen.train_from_file(fileInput)#, new_model=True, max_length=3, num_epochs=2, gen_epochs=1, word_level=True)
    textgen.train_from_file('resource/built.txt')
#    textgen.generate()
#    textgen.generate_to_file('outputs/built.txt')
    # generate text from the model
#    textgen.generate_to_file(fileOutput, n=200)



#generate_text(inDir+"/accomplishments.txt", outDir+"/accomplishments.txt")
'''
generate_text(inDir+"/built.txt", outDir+"/built.txt")
generate_text(inDir+"/challenges.txt", outDir+"/challenges.txt")
generate_text(inDir+"/does.txt", outDir+"/does.txt")
generate_text(inDir+"/inspiration.txt", outDir+"/inspiration.txt")
generate_text(inDir+"/learned.txt", outDir+"/learned.txt")
generate_text(inDir+"/next.txt", outDir+"/next.txt")
'''
