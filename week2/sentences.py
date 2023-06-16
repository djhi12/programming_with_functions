import random


def main():
    words = ["boy", "girl", "cat", "dog", "bird", "house"]
    word = random.choice(words)
    cap_word = word.capitalize()
    # print(cap_word)

    for _ in range(6):  # Call make_sentence six times
        quantity = random.randint(1, 3)  # Random quantity: 1, 2, or 3
        # Random tense: past, present, or future
        tense = random.choice(["past", "present", "future"])

        sentence = make_sentence(quantity, tense)
        print(sentence.capitalize())


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    sentence = f"{determiner} {noun} {verb}."
    return sentence


def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    determiner = random.choice(determiners)
    return determiner


def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think",
                 "will run", "will sleep", "will talk", "will walk", "will write"]
    else:
        print("Type the correct tense.")
        return None

    verb = random.choice(verbs)
    return verb


main()
