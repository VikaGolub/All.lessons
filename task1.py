print("Beautiful is better than ugly. \nExplicit is better than implicit. \nSimple is better than complex. \nComplex is better than complicated. \nFlat is better than nested. \nSparse is better than dense. \nReadability counts. \nSpecial cases aren\'t special enough to break the rules.\nAlthough practicality beats purity. \nErrors should never pass silently. \nUnless explicitly silenced. \nIn the face of ambiguity, refuse the temptation to guess. \nThere should be one—and preferably only one—obvious way to do it. \nAlthough that way may not be obvious at first unless you're Dutch. \nNow is better than never. \nAlthough never is often better than right now. \nIf the implementation is hard to explain, it\'s a bad idea. \nIf the implementation is easy to explain, it may be a good idea. \nNamespaces are one honking great idea—lets do more of those!")
print('\n')
zen_of_python = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

better =  zen_of_python.count ("better")
print("words: 'better' in zen is: " + str(better))

never = zen_of_python.count ("never")
print("words 'never' in zen is: " + str(never))

is_word = zen_of_python.count ("is")
print("words 'is' in zen is: " + str(is_word))

print("\n")
print (zen_of_python.upper())
print(zen_of_python.replace ("i", "&"))