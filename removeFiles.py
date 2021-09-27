import os, time, shutil
path = input("Path to be searched in. ")
seconds = time.time() - (15 * 86400)

if os.path.exists(path):
  for root, dirs, files in os.walk(path, topdown=True):
    for name in files:
      path = os.path.join(root, name)
      ctime = os.stat(path).st_ctime
      if seconds >= ctime:
        os.remove(path)
    for name in dirs:
      path = os.path.join(root, name)
      ctime = os.stat(path).st_ctime
      if seconds >= ctime:
        shutil.rmtree(path)
else : print("404 : path not found")
