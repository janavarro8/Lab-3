"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Option B
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 11/4/18
Purpose: Find the combinations of 
"""
import AVL
import RedBlack

def main():
    userInput = 'z'     #will hold user's input. Set to 'z' to enter loop.
    tree = None         #will hold tree
    fileName = ""       #will hold file name for tree creation
    validInput = False  #will hold if input is valid
    count = [1]         #will be passed to count anagrams 
    count[0] = 0        #allows me to not have to return a value from function
    
    while(userInput == 'z'):
        userInput = input("Enter 'A' for an AVL tree or 'B' for a red-black tree: ")
        userInput = userInput.lower()                   #set to lowercase to accept capitals too
        if(userInput != 'a' and userInput != 'b'):      #checks for invalid input
            print("Error. Input must be 'a' or 'b'.")
            userInput = 'z'
    
    while(validInput == False):
        fileName = input("Enter the name of your file: ")
        try:
            if(userInput == 'a'):
                tree = AVL.AVLTree()            #creates AVL tree
            else:
                tree = RedBlack.RedBlackTree()  #creates Red-Black tree
            create_tree(tree, fileName, userInput)
            validInput = True                   #set to true to exit loop
        except FileNotFoundError:
            print("File not found. Try again.")
    
    userInput = input("Enter a word to find anagrams for:")
    
    temp = tree
    print()
    print("Anagrams for '", userInput, "':")
    print_anagrams(userInput, "", temp)
    
    print()
    
    temp = tree
    print("Total Anagrams: ")
    count_anagrams(userInput, "", temp, count)
    
    print(count[0])
    
    print("\n---------------------------------")
    
    validInput = False
    while(validInput == False):
        fileName = input("Enter the name of your next file: ")
        try:
            temp = tree
            print()
            max_anagrams(temp, count, fileName)
            validInput = True                   #set to true to exit loop
        except FileNotFoundError:
            print("File not found. Try again.")
    
    """temp = tree          #prints contents of tree in order
    print_tree(temp.root)"""

def create_tree(tree, fileName, userInput):
    with open(fileName, "r") as file:       #opens file with given fileName
        for i in file:                      #i holds each line in the file
            line = i.split()
            line[0] = line[0].lower()
            if(userInput == 'a'):
                tree.insert(AVL.Node(line[0]))  #inserts to AVL tree
            else:
                tree.insert(line[0])            #inserts to Red-Black tree

#prints tree in order            
def print_tree(node):
    if(node is None):
        return
    print_tree(node.left)
    print(node.key)
    print_tree(node.right)

#prints all anagrams of a given word    
def print_anagrams(word, prefix, tree):
    temp = tree
    
    if len(word) <= 1:
        str = prefix + word
        
        if(temp.search(str) == True):   #looks for str in the tree
            print(str)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur, tree)

#counts how many anagrams a given word has    
def count_anagrams(word, prefix, tree, count):
    temp = tree
    
    if len(word) <= 1:
        str = prefix + word
        
        if(temp.search(str) == True):   #looks for str in the tree
            count[0] += 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated.
                count_anagrams(before + after, prefix + cur, tree, count)

#finds the word with the maximum amount of anagrams
def max_anagrams(tree, count, fileName):
    maxAnagrams = 0     #will hold the max number of anagrams
    maxWord = ""        #will hold the word with max num of anagrams
    temp = tree         #temp variable for tree
    
    with open(fileName, "r") as file:                   #opens file 
        for i in file:                                  #stores each line in i
            count[0] = 0                                #set back to 0 to count anagrams again
            line = i.split()                            #takes first element of line
            count_anagrams(line[0], "", temp, count)
            
            if(count[0] > maxAnagrams):
                maxAnagrams = count[0]
                maxWord = line[0]
            temp = tree
    
    print("The word with the most anagrams is '", maxWord, "' with ", maxAnagrams, " anagrams.")
    print("The anagrams for '", maxWord, "' are:")
    print_anagrams(maxWord, "", temp)
    
      
main()