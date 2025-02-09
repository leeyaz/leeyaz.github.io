

letters = []
print("enter the letters: \n")

for i in range(7):
    user_input = input()
    letters.append(user_input)
         

print(letters)

req = input("what is the required letter? \n")

if req not in letters:
    print("please use a letter in the letters mentioned earlier")
    req = input("what is the required letter? \n")
else:
    pass

print(f"{letters} \n required letter: {req} \n")

def sort(least, most):
    strLetters = "".join(letters)

    link = 'wordlist_cs11ref.txt'
    with open(link, 'r') as file:
            word_list = [word.strip() for word in file]
    file.close()

    for word in word_list:
        if req in word and set(word).issubset(set(strLetters)):

            #for limits of words
            if least != "none" and most != "none":
                 if len(word) >= int(least) and len(word) <= int(most):
                      print(word)
                 else:
                      pass

            if least and most == "none":
                print(word)
            

print(sort("none", "none"))

user_input1 = input("least amount of letters? \n (if not int = pass)\n")
user_input2 = input("most amount of letters? \n (if not int = pass)\n")

if user_input1.isdigit() and user_input2.isdigit():
    print(sort(user_input1, user_input2))
elif user_input1.isdigit() == False and user_input2.isdigit():
    print(sort(0, user_input2))
elif user_input1.isdigit() and user_input2.isdigit() == False:
    print(sort(user_input1, 1000000))
else:
     pass