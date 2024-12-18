        #3. Add content to an existing file without overwriting
f = open("/home/jesna/workspace/repoo/sample/content1.txt","a")
if f:
    f.write("Enjoy your Day")
f.close()

#red=ading 
f = open("/home/jesna/workspace/repoo/content.txt","r")
print(f.read())