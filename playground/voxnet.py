import os, glob
import subprocess

#BINVOX=~/Downloads/binvox  # Change to path of binvox
#DATA=/media/jarvis/pubData/ShapeNetData/bag/*/models/*.obj  


files = glob.glob("/media/jarvis/pubData/ShapeNetData/bag/*/models/*.obj")

print files