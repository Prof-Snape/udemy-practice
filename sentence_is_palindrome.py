def palindrome(sent: str) -> bool:
    """
    Check if the sentence is a palindrome.

    The function will trim all non-alphanumeric characters from the sentence then convert every `str` in lowercase
    and check if it equals to when it is reversed.

    :param sent: The sentence that user will check for palindrome.
    :return: The boolean expression True if the sentence is a palindrome else False.
    """
    sent = "".join(i for i in sent if i.isalnum())
    return sent[::-1].casefold() == sent.casefold()


sentence = "Was it a car, or a cat, I saw?"
sentence_2 = "Do geese see god?"
sentence_3 = "Desnes not far, Rafton sensed."
sentence_4 = "Not a palindrome sentence."

print(palindrome(sentence))
print(palindrome(sentence_2))
print(palindrome(sentence_3))
print(palindrome(sentence_4))
