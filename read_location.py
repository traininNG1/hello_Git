        #4. Read content of a file from a specific position
f = open("/home/jesna/workspace/repoo/sample/content1.txt","r")
print("File pointer is at position :",f.tell())
content = f.read();
print("Now the file pointer is at position:",f.tell())