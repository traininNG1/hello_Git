        #5.Write a program to delete all files in a folder
import os

def delete_folder(folder_path):
    for item in os.listdir(folder_path):
         item_path = os.path.join(folder_path, item)
         os.remove(item_path)
    #remove the empty folder
    os.rmdir(folder_path)
    print(f"The folder {folder_path} has been deleted successfully.")


folder_path = "/home/jesna/workspace/repoo/sample"
delete_folder(folder_path)