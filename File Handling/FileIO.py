# First method :
print(" Studing File handling in python::")

f=open('Text.txt','r')    # Read mode
display=f.read()
print(display)
f.close()


f=open('Text2.txt','w')    # Write mode
content=f.write('Writing content in Text2 file \n')
f.close()

f=open('Text.txt','a')     # Append mode
text=f.write('\n Writing in Text file in append mode ')
f.close()


# another way of IO in python-->

with open('Text2.txt','a') as f:
 f.write('\n  Writing in Text2 file in apppend mode with 2 method it does not need close command in end')
# This method does not need to close file 

