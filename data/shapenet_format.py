import glob
import shutil 
import os
import subprocess
import progressbar


file_paths = ['/media/jarvis/pubData/ShapeNetData/mug/*/models/model_normalized.obj']
out_dirs = ['/media/jarvis/pubData/ShapeNetData/mug/binvox/']

for file_path, out_dir in zip(file_paths, out_dirs):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    #print 'Copying Files in this format: %s' % file_path
    files = glob.glob(file_path)
    #print files
    pbar = progressbar.ProgressBar(maxval=len(files)+1).start()
    for i, _file in enumerate(files):
        new_name = os.path.abspath(_file)
        new_name = os.path.basename(os.path.dirname(os.path.dirname(new_name))) + '.binvox'
        #size needs to be (100, 32, 32, 32, 1)
        #when using default -d 256 size is (100, 256, 256, 256, 1)
        # when using -d 32 size is 
        bashCommand = "/home/jarvis/Downloads/binvox %s -e -d 32" %_file
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        process.communicate()  # Wait until binvox finished
        shutil.move(_file.replace('.obj', '.binvox'), out_dir+new_name)  # copy file to new dir
        pbar.update(i)
    pbar.finish()
