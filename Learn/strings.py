# working with strings, manipulating cases
fName = "weltron"
lName = "bitange"
name = fName + " " + lName
print(name.title())  # changes first letter of each word to upper case
print(name.upper())  # changes entire string to upper case
print(name.lower())  # changes to lower case
print(
    name.strip()
)  # removes whitespace .rstrip to the right and .lstrip to the left, strip for both
print(
    "\t" + fName + "\n\t" + lName
)  # \n adds new line, \t adds whitespace/indentation to output
names = input("What is your name?").strip().title()
first, last = names.split(" ")
print(f"Hello, {last}")
