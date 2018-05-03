# Find if the word is palindrome or not..

user_input= input("Enter a word to find : ")

user_word_lower = user_input.lower()

word_length = len(user_word_lower)

redo = True

reverse_word = ""
def palindrome(user_word,length_word,reverse_text):
    

    for letter in range(length_word-1,-1,-1):
        reverse_text = reverse_text + user_word[letter]
    return reverse_text


reverse_word = palindrome(user_word_lower,word_length,reverse_word)

if (reverse_word == user_word_lower):
    print(f"The word {user_input} is a palindrome.")
else:
    print(f"The word {user_input} is not a palindrome.")  




 

     
    
