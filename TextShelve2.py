import shelve
sh=shelve.open("Shelve2")
print(list(sh.items()))
