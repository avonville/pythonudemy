def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in text:
        if char not in alphabet:
            end_text += char
            continue
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = ""
while should_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    should_continue = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
