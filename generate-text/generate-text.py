from textgenrnn import textgenrnn

outDir = "outputs"
inDir = "resource"

def generate_text(fileInput, fileOutput, lines):
    textgen = textgenrnn()
    # train the model
    textgen.train_from_file(fileInput, new_model=True, max_length=3, num_epochs=2, gen_epochs=1, word_level=True)
    # generate to file
    textgen.generate_to_file(fileOutput, n=lines)


generate_text(inDir+"/accomplishments.txt", outDir+"/accomplishments.txt", 50)
generate_text(inDir+"/built.txt", outDir+"/built.txt", 50)
generate_text(inDir+"/challenges.txt", outDir+"/challenges.txt", 50)
generate_text(inDir+"/does.txt", outDir+"/does.txt", 50)
generate_text(inDir+"/inspiration.txt", outDir+"/inspiration.txt", 50)
generate_text(inDir+"/learned.txt", outDir+"/learned.txt", 50)
generate_text(inDir+"/next.txt", outDir+"/next.txt", 50)
generate_text(inDir+"/subtitles.txt", outDir+"/subtitles.txt", 1)
generate_text(inDir+"/titles.txt", outDir+"/titles.txt", 1)
