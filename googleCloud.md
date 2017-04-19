# Setup ssh key

```ssh-keygen -t rsa -f ~/.ssh/my-ssh-key -C [USERNAME]
chmod 400 ~/.ssh/my-ssh-key
cat ~/.ssh/my-ssh-key.pub
```

Copy pub to google key pair in console for a particular project or instance. Then you can ssh into it (:

#You may need to request limit for adding GPUs
# Create VM then install CUDA, Instructions are for ubuntu 16.04 LTS


echo "Checking for CUDA and installing."
# Check for CUDA and try to install.
```
#!/bin/bash
if ! dpkg-query -W cuda; then
  # The 16.04 installer works with 16.10.
  curl -O http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
  dpkg -i ./cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
  apt-get update
  apt-get install cuda -y
fi
```
