import random


def main():
    words = ["boy", "girl", "cat", "dog", "bird", "house"]
    word = random.choice(words)
    cap_word = word.capitalize()

    for _ in range(6):
        quantity = random.randint(1, 3)
        tense = random.choice(["past", "present", "future"])

        sentence = make_sentence(quantity, tense)
        print(sentence.capitalize())


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    adverb = get_adverb()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)

    sentence = f"{determiner} {adjective} {noun} {verb} {adverb} {prepositional_phrase1} {prepositional_phrase2}."
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


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase


def get_adjective():
    """Return a randomly chosen adjective from a list of adjectives.

    Return: a randomly chosen adjective.
    """
    adjectives = ["beautiful", "smart", "funny", "tall", "brave",
                  "kind", "friendly", "creative", "happy", "strong"]

    adjective = random.choice(adjectives)
    return adjective


def get_adverb():
    """Return a randomly chosen adverb from a list of adverbs.

    Return: a randomly chosen adverb.
    """
    adverbs = ["quickly", "carefully", "eagerly", "happily", "loudly",
               "gracefully", "patiently", "silently", "vigorously", "warmly"]

    adverb = random.choice(adverbs)
    return adverb


main()
