#dump()
#load()

import pickle
fp=open("pickle.txt","wb")
obj=["dhoni","sharu","sony"]
pickle.dump(obj,fp)
fp.close()
