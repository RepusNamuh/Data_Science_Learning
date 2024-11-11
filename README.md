# How the jupyter notebook work

This repository is simply where I learn the basic of Data Science. I always create function in a folder called library and test those function in a folder called Learning

Learning contains jupyter notebooks, where I will import function to run

However, if this repo is run on VSCode, you can potentially encounter an import error in the Notebook itself saying there is no module called library

This problem can be fix easily by adding the path of the main folder to the current jupyter notebook you are using that is

sys.append(r"(the path you store the repo)\Data_Science")

This will ensure that the library path will always be found