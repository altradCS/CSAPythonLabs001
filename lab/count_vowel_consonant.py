def count_alphabet(filename):
    vowels = {"A", "E", "I", "O", "U"}

    vowel_count = 0
    consonant_count = 0

    try:
        with open(filename, "r") as file:
            content = file.read()

        for i in content:
            if i.isalpha():
                uppercase_i = i.upper()

                if uppercase_i in vowels:
                    vowel_count += 1

                else:
                    consonant_count += 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")


filename = input("Enter a text filename: ")
count_alphabet(filename)
