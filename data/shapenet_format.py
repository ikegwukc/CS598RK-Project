import glob
from shutil import copyfile
import os
import progressbar


file_paths = ['/media/jarvis/pubData/ShapeNetData/mug/*/models/model_normalized.solid.binvox', '/media/jarvis/pubData/ShapeNetData/bag/*/models/model_normalized.solid.binvox']
out_dirs = ['/media/jarvis/pubData/ShapeNetData/mug/binvox/', '/media/jarvis/pubData/ShapeNetData/bag/binvox/']

for file_path, out_dir in zip(file_paths, out_dirs):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    #print 'Copying Files in this format: %s' % file_path
    files = glob.glob(file_path)
    #print files
    pbar = progressbar.ProgressBar(maxval=len(files)+1).start()
    for i, _file in enumerate(files):
        new_name = os.path.abspath(_file)
        new_name = os.path.basename(os.path.dirname(os.path.dirname(new_name))) + '.solid.binvox'
        #print out_dir+new_name
        copyfile(_file, out_dir+new_name)
        pbar.update(i)
    pbar.finish()