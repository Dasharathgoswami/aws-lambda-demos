import os

os.chdir('/home/dashrath/Desktop/js')

# Am I in the correct directory?
#print(os.getcwd())
 
#print(dir(os))
for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)
    print(file_name)
