import os
import shutil
from datetime import datetime
current_time = datetime.now()
source = "C:/Users/Tommaso/Desktop"
base_path= "C:/"
full_path = os.path.join(base_path, current_time.strftime("%Y-%m-%d_%H-%M-%S"))
os.mkdir(full_path)
allfiles = os.listdir(source)
for f in allfiles:
    src_path = os.path.join(source, f)
    dst_path = os.path.join(full_path, f)
    shutil.move(src_path, dst_path)
    print("Moved file {} to {}".format(src_path, dst_path))



print("Done!")