import shelve
sh=shelve.open("Shelve2")
with shelve.open("shelve2")as sh:
    sh['1']="laxmi"
    sh['2']="sangee"
    sh['3']="mounika"
sh.close()