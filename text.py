
def name_case(text):
    word_list = text.split()
    full_name = ""
    for word in word_list:
        word = word.capitalize()
        full_name += f"{word} "
    return full_name.strip()

    # return text.capitalize()
    # word_list = text.split()
    # full_name = ""
    # for word in word_list:
    #     name = text[0].upper() + text[1:].lower()
    # return name


def initials(text):
    word_list = text.split()
    result = ""
    for word in word_list:
        initial = word[0].upper() + "."
        result += f"{initial}"
    return result


print(name_case("JONAS JONAITIS"))
print(initials("Labas vakars, Lietuva"))

