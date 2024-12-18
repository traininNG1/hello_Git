        #2.Read the conent of a file  and print it
try:
    with open("/home/jesna/workspace/repoo/sample/content1.txt","r") as f:
        content = f.read()
        print(content)
except IOError:
    print("Error: could not read the file")
