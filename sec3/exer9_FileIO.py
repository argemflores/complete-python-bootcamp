# Write a script that opens a file named 'test.txt', writes 'Hello World' to the file, then closes it
# Example
# f = open('test.txt', 'w')
# f.write('Hello World')
# f.close()
with open('test.txt', mode='w') as f:
    f.write('Hello World')
