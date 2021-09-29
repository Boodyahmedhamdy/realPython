from win10toast import ToastNotifier
from tqdm import tqdm
import time
box = ToastNotifier()

# box.show_toast("this is a heading", "this is some paragraph")

for i in tqdm(range(20)):
    time.sleep(0.5)

box.show_toast("loop has ended", "everything is done")
