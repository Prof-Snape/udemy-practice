def palindrome(sent):
    sent = "".join(i for i in sent if i.isalnum())
    return sent[::-1].casefold() == sent.casefold()


sentence = "Was it a car, or a cat, I saw?"
sentence_2 = "Do geese see god?"
sentence_3 = "Desnes not far, Rafton sensed."

print(palindrome(sentence))
print(palindrome(sentence_2))
print(palindrome(sentence_3))
