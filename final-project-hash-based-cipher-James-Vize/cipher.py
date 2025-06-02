#James Vize
#Cipher.py
#Hash-based cipher 
#takes the ordinal position of a letter and the frequency and shifts the value
#it then encodes the message displaying both the hashing for each letter and the message. 


#Function to calculate the shift for letter based on frequency
def calculateShift(letter, frequency):
    #Determine the position of the letter in alphabet
    #for this code 'a' will be 1 and etc
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ordinalPos = alphabet.index(letter.lower()) +1
    #calculate the shift value using the frequency and position
    shiftValue = frequency * ordinalPos
    return shiftValue

#Function to encode the message using the shift value
def encodeMessage(message):
    #Defines the alphabet as a list of lowercase letters
    #using list() as it can hold all multiple elements rather than just 1 like an array
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    #Start a dictionary to count the frequency of each letter in the message
    #Store each letter as a key and then its frequency as a value
    frequencyDict = {letter: 0 for letter in alphabet}

    #Time to count the frequency of each letter in the message
    for letter in message:
        if letter.isalpha(): #like stated on canvas checks if the character is a letter
            frequencyDict[letter.lower()] += 1 #increment the frequency

    #Set an empty string to store the encoded message
    encodedMessage = ''

    #Now we encode each letter in the message
    for letter in message:
        if letter.isalpha(): #again checks the character to make sure its a letter
            #calculate the shift value for the letter
            shiftValue = calculateShift(letter, frequencyDict[letter.lower()])

            #This is to determine the new position for the letter
            isUpper = letter.isupper()
            originalIndex = alphabet.index(letter.lower())
            #makes sure alphabet wraps using formula provided
            newIndex = (originalIndex + shiftValue - 1) % 25 + 1

            #get the shifted letter 
            shiftedLetter = alphabet[newIndex]

            #we need to also make sure that the encoded message matches any uppercase letters
            if isUpper:
                shiftedLetter = shiftedLetter.upper()

            #adding the shifted letter to the encoded message
            encodedMessage += shiftedLetter
        else:
            #this is to add anything thats not a letter to the encoded message
            encodedMessage += letter

    #Return the encoded message and the dictionary
    return encodedMessage, frequencyDict

#NOW we display the frequency of each letter in the alphabet
def displayHashing (frequencyDict):

    #define the alphabet again
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #print the frequency for each letter in the alphabet
    for letter in alphabet:
        print(f"{letter}: {frequencyDict[letter]}")

#main function that displays everything 
def main():
    #prompt the user to enter a message to encode
    inputMessage = input('Enter your message: ')

    #encode the message and obtain the frequency dictionary
    encodedMessage, frequencyDict = encodeMessage(inputMessage)

    #print the encoded message
    print('Encoded message:', encodedMessage)

    #display the hashing 
    print('Hashing:')
    displayHashing(frequencyDict)

main()