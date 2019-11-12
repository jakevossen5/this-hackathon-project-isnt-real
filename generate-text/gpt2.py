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

#    tf.variable_scope("sess", reuse=True)
     
    '''
    gpt2.finetune(sess,
        "resource/"+inputFile+".txt",
        model_name=model_name,
        #run_name=inputFile,
        overwrite=True,
        steps=2)
        #_traceback = tf_stack.extract_stack())   # steps is max number of training steps    ''' 
        
        
    # generate 50 examples
    for x in range(0,10):
      #  tf.get_variable_scope().reuse_variables()
        gpt2.load_gpt2(sess)
      #  output = gpt2.generate(sess, return_as_list=True)[0]
        gpt2.generate_to_file(sess, destination_path="newoutputs/" +outputDir+str(uuid.uuid4())+".txt")

#        datalist = gpt2.generate(sess, return_as_list=True)[0]
#        print (datalist)
#        gen_to_file(outputDir, inputFile)
 #       tf.get_variable_scope(reuse=True)
        #tf.get_variable_scope().reuse_variables()

#    tf.get_variable_scope(reuse=True)
#    tf.AUTO_REUSE = True
#    sess.reuse_variables()
   # tf.reset_default_graph()
    gpt2.reset_session(sess,threads=-1,server=None)
    '''
        print("here")
        #tf.get_variable_scope().reuse_variables()
        gpt2.load_gpt2(sess)
#        t = gpt2.generate(sess)
     #   gpt2.generate_to_file(sess, destination_path="newoutputs/" +outputDir+str(uuid.uuid4())+".txt")
        output = gpt2.generate(sess, return_as_list=True)[0]
#        print (type(t))
#        output = str(gpt2.generate(sess))
        gen_to_file(outputDir, output) 
        #tf.get_variable_scope().reuse_variables()
        #raise failingThread.exc_info[1].with_traceback(failingThread.exc_info[2])
        '''
        
#    os.rename("checkpoint
    
#train_data ("accomplishments", "accomplishments/")
#train_data ("challenges", "challenges/")
#train_data ("built", "how_we_build/")
#train_data ("inspiration", "insp/")

#train_data ("does", "what_it_does/")
#train_data ("learned", "what_learned/")
train_data ("next", "whats_next/")
train_data ("subtitles", "sub_title/")
train_data ("titles", "title/")


#### ran
