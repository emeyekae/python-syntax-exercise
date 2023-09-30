
def print_upper_words(words,must_start_with):
    """Returns UPPER CASE "words" that start with letter/s in  "must_start_with"
       "words" is a list of strings.  "must_start_with" is a set of letters.

        Example: 
        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y"})

        # this should print "HELLO", "HEY", "YO", and "YES"

    """

    for letter in must_start_with:
        for word in words:
            if ( word[0].upper() == letter.upper() ):
                print(word.upper())
    return

