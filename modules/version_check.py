
from operator import le
import os
import json


"""
return true if the current version is greater than the specified version
    True=version satisfy
    False=Unsatisfy
"""
def check_version(version,current_version):
    version=version.split(".")
    current_version=current_version.split(".")
    n=max(len(version),len(current_version))
    #print(current_version,n)
    if len(version)!=n:
        while(len(version)<n):
            version=version+['0']
    if len(current_version)!=n:
        while(len(current_version)<n):
            current_version=current_version+['0']
    """Using 2 pointer method to check version"""
    for i in range(n):
        if int(version[i])==int(current_version[i]):
            continue
        elif int(version[i])>int(current_version[i]):
            # i.e the version required is greater
            return False
        else:
            return True
    return True

    





"""Tesing the function"""
# ans=check_version("4.11.4.5","4.11.3.5")
# print(ans)