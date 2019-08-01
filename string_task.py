print("\nMad libs where libs get Mad\n")

number = input("Please provide a number:  ")
noun = raw_input("Please provide a noun:  ")
name = raw_input("Please provide a full name:  ")
any_sentence = raw_input("Please provide a sentence:  ")
verb = raw_input("Please provide a verb:  ")

mad_lib = """

    It was {} o'clock when I heard a knock at the door...
    I opened the door and there was a box full of {} with a note saying "From {}".
    Just as I closed the door I heard a scream "{}!"
    I froze in place and all I could do was {}.	

    """ 

print(mad_lib.format(number, noun, name.title(), any_sentence.upper(), verb))