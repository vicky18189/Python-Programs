# import re
# import os


# def renamefiles():
#     file_list = os.listdir(r"E:\prank\prank")
#     os.chdir(r"E:\prank\prank")
#     saved_path = os.getcwd()
    # print("Current Working Dir. is " + saved_path)

    # for file_name in file_list:
# new_name = re.sub('[0-9]', '', '2chennai.jpg')
#         os.chdir(saved_path)
# renamefiles()

# import os
# def renamefiles():
#     file_list = os.listdir(r"E:\prank\prank")
#     # print(file_list)
#     saved_path = os.getcwd()
#     # print("Current Working Dir. is " +saved_path)


#     for file_name in file_list:
#         os.rename(file_name, file_name.strip("0123456789"))
#         os.chdir(saved_path)

# renamefiles()

import os
def renamefiles():
    name_list=os.listdir(r"E:\prank\prank")
    print(name_list)
    saved_path=os.getcwd()
    print("Current working directory is"+saved_path)
    os.chdir(r"E:\prank\prank")

    for file_name in name_list:
        print("old name"+file_name)
        print("new name"+file_name.strip("0123456789"))
        os.renames(file_name,file_name.strip("0123456789"))
    os.chdir(saved_path)

renamefiles()