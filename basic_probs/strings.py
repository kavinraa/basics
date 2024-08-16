def checkIfPangram(sentence: str) -> bool:
    # convert sentence to set, to get letters without duplicate
    set_sent = set(sentence)

    # Get the length of letters in the set 
    unique_letters = len(set_sent)
    
    # check if equal to 26, since english alphabets == 26
    return len(unique_letters) == 26
    
sentence = "thequickbrownfoxjumpsoverthelazydog"
result  = checkIfPangram(sentence)
print(result)