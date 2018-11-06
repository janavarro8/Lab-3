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
    print("Anagrams: ")
    print_anagrams(userInput, "", temp)
    
    print()
    
    temp = tree
    print("Total Anagrams: ")
    count_anagrams(userInput, "", temp, count)
    
    print(count[0])
    
    """temp = tree          #prints contents of tree in order
    print_tree(temp.root)"""
    
    """temp = tree
    maxAnagrams = max_anagrams(temp, temp.root)
    print(maxAnagrams)"""

def create_tree(tree, fileName, userInput):
    with open(fileName, "r") as file:   #opens file with given fileName
        for i in file:                      #i holds each line in the file
            line = i.split()
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
def max_anagrams(tree, root):
    temp = tree
    count = [1]
    count[0] = 0
    
    if(temp == None):
        return 0
    
    count_anagrams(temp.root.key, "", temp, count) #num anagrams for root
    
    maxAnagrams = count[0] #assume root is max
    
    temp = tree
    leftMax = max_anagrams(temp, temp.root.left)    #max from left tree
    temp = tree
    rightMax = max_anagrams(temp, temp.root.right)  #max from right tree
    
    if(leftMax > maxAnagrams):
        maxAnagrams = leftMax
    if(rightMax > maxAnagrams):
        maxAnagrams = rightMax
        
    return maxAnagrams
    
    
      
main()