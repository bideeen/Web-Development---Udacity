# step 1 : get all the file names
# step 2 : for each file rename it

import os
def rename_files():
    # 1 get files names from folder
    file_list = os.listdir(r"/home/bideen/Desktop/Web Development - Udacity/prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"/home/bideen/Desktop/Web Development - Udacity/prank")
    path = os.getcwd()
    print(path)

    # 2 for each file, rename filename
    for file_name in file_list:
        # used to rename the files
        os.rename(file_name, file_name.translate({ord(c):'' for c in "0123456789"}))
    os.chdir(saved_path)

rename_files()