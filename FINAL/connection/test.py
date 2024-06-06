import sys
sys.path.append('../')

from database import connect

rows = connect.get()
var = connect.verify_credentials('user1',12345)
if var is True:
    print("found")
else:
    print("not found")

connect.insert()