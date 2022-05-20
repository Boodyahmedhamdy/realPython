# import platform  # to know the platform
import subprocess

# # name of the system i am currently running
# print(platform.system())
#
# # version you are using
# print(platform.release())

# to run another process
# print(subprocess.run(["python", "test.py"]))

# running ls command or dir
res = subprocess.run(["git", "status"], capture_output=True)
print(f"{res.returncode = }")
print(f"{res.stderr = }")
print(res.stdout.decode())


print(subprocess.run("dir", shell=True, capture_output=True).stdout.decode())



