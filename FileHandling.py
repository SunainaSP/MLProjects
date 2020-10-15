import os

f = open('File.txt', 'w')
print('FILE CREATED SUCCESSFULLY!!')
f.write('Every global constitution begins with a proposal or a preface.')
print('DATA WRITTEN SUCCESSFULLY!!')
f.close()

# appending to the contents of the file
f = open('File.txt', 'a')
f.write('\nSimilarly, Indian constitution too begins with the proposal.')
print('DATA APPENDED SUCCESSFULLY!!')

# reading the contents of the file
f = open('File.txt', 'r')
call = f.read()
print(call)
print('DATA READ SUCCESSFULLY!!')
f.close()

# cropping the file contents
f = open('File.txt', 'r')
call = f.read(5)
print(call)
print('DATA SLICED SUCCESSFULLY!!')
f.close()

# counting characters in the file
f = open('File.txt', 'r')
data = f.read().replace(" ", "")
NumofChars = len(data)
print('Number of characters is', NumofChars)
