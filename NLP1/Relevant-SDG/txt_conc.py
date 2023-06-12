import shutil
with open('output_file.txt','wb') as wfd:
    for f in range(4000):
        try:
            with open(str(1016+f)+".txt",'rb') as fd:
                shutil.copyfileobj(fd, wfd)
        except:
            ...