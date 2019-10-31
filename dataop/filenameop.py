import os
from glob2 import glob
import datetime
import time

print('now:', time.time())
row = 1
dataDirName = 's46-data-15/'
for name in glob(dataDirName + 'W0*.CSV'):
    # print('\t', name)
    
    file_info = os.stat(name)
    # print(file_info.st_size)
    # print(file_info.st_atime)
    # print(file_info.st_mtime)
    now_ts = datetime.datetime.fromtimestamp(file_info.st_mtime)

    # print(now_ts.strftime('%Y%m%d_%H%M%S'))
    now_ts_str = now_ts.strftime('%Y%m%d_%H%M%S')
    os.rename(name, dataDirName+'W'+now_ts_str+'.CSV')
#     print(file_info.st_ctime)
#     dtStr =
    # time = name[-19:-4]
#     dt = datetime.datetime.strptime(time, "%Y%m%d_%H%M%S")
#     dtStr = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    row+=1