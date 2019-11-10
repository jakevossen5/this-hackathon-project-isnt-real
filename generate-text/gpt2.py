import gpt_2_simple as gpt2
import tensorflow as tf
import uuid
#import os

model_name = "124M"

# this takes a very long time, it only needs to be done once ever
#gpt2.download_gpt2(model_name=model_name)

# function to put text in a file
def gen_to_file (filedir, text):
    with open("newoutputs/"+filedir+str(uuid.uuid4())+".txt", 'w') as outputFile:
        print (text)
        outputFile.write(text)

# function to get the words trained from each category
def train_data (inputFile, outputDir):
    sess = gpt2.start_tf_sess()
    # train for the input file 
    gpt2.finetune(sess,
        "resource/"+inputFile+".txt",
        model_name=model_name,
        run_name=inputFile,
        steps=10)   # steps is max number of training steps 
     
    # generate 50 examples
    for x in range(0,15):
        print("here")
        #tf.get_variable_scope().reuse_variables()
        gpt2.load_gpt2(sess)
        output = str(gpt2.generate(sess))
        gen_to_file(outputDir, output) 
        tf.get_variable_scope().reuse_variables()
#    os.rename("checkpoint
    
train_data ("accomplishments", "accomplishments/")
train_data ("challenges", "challenges/")
train_data ("built", "how_we_build/")
train_data ("inspiration", "insp/")
train_data ("subtitles", "sub_title/")
train_data ("titles", "title/")
train_data ("does", "what_it_does/")
train_data ("learned", "what_learned/")
train_data ("next", "whats_next/")
