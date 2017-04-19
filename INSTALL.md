## Install these Dependencies
- numpy-stl ```pip install numpy-stl```
-tensorflow 0.12 ```https://www.tensorflow.org/versions/r0.12/get_started/os_setup ```
With tensorflow the easiest thing to do is to pip install. For Google Cloud we may use GPU implementation to get results back faster but for now use CPU implementation...

- binvox http://www.patrickmin.com/binvox/
This is used to convert files to .binvox for the network...
-binvox-rw-py https://github.com/dimatura/binvox-rw-py
Python wrapper to read and write .binvox files
- viewvox http://www.patrickmin.com/viewvox/
Useful for viewing binvox files

## Other Things
- meshlab is useful for viewing .stl, .obj files, etc. ``` sudo apt-get install meshlab```



## Google Cloud
Datalab basically uses ipython notebooks and can use gpus.
To start:
- Enable Google Cloud Shell
-  

https://cloud.google.com/datalab/docs/quickstarts