import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(choice,original_text, shift_amount):
    output_word = ""
    if choice == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        if letter not in alphabet:
            output_word += letter
            
        else:
            new_position = (alphabet.index(letter) + shift_amount) 
            new_position %= len(alphabet)
            output_word += alphabet[new_position]
        
    print(f"This is the {choice}d result: {output_word}") 

run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(choice = direction, original_text= text, shift_amount= shift)

    restart = input("Do you want to encode/decode another message?\n").lower()
    if restart == "no":
        run = False
