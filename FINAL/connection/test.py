import sys
sys.path.append('../')

from database import connect

rows = connect.get()
var = connect.verify_credentials('user11',12345)
if var is True:
    print("found")
else:
    print("not found")