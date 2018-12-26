import combine
import cutw
import cutr
import os
f = "redo2"
d = os.listdir(f)
print(d)

for i in range(len(d)):

    newname = f+"/"+d[i]
    cutw.cal(newname)
    print("cancer is ready")
    cutr.cal(newname)
    print("t cell is ready")
    combine.cal(newname)
    print("combine is ready")
