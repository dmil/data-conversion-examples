# Read from name.txt
with open('name.txt') as f:
    my_name = f.read()

# Write the contents of name.txt and hello
with open('hello.txt', 'w') as f:
    f.write('who is ' + my_name)

