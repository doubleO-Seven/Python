a = input("Enter a string: ") [::-1]
print(a)


# remove dupicate
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)