import os,platform
os.system("git pull")
rmx=platform.architecture()[0]
if rmx=='64bit':
  import CR
if rmx=='32bit':
  import CR2
else:print('\033[1;32m[•] Contract Admin For Help');exit()
