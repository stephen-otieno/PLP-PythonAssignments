file_path = "input.txt"

#Reading the content of input.txt
with open(file_path, 'r') as file:
    content = file.read()
    

#Counting the number of words in input.txt file

words = content.split()
words_count = len(words)


#Converting all texts to uppercase

words_uppercase = content.upper()


#Writing processed texts to output.txt
outputFile_path = "output.txt"

with open(outputFile_path, "w") as file:
    file.write(words_uppercase)
    file.write(f"\n Number of Words counted: {words_count}")
    print(f"\n{outputFile_path} file was created successfully!")
