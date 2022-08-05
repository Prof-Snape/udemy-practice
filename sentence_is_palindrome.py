def palindrome(sent):
    sent = "".join(i for i in sent if i.isalnum())
    return sent[::-1].casefold() == sent.casefold()


sentence = "Was it a car, or a cat, I saw?"
print(palindrome(sentence))
