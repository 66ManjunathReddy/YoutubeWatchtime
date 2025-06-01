import webbrowser
import time

url = "https://youtube.com/yourvideoURL"

for i in range(20000):
    webbrowser.open_new_tab(url)
    time.sleep(0.1)  # Adjust delay as needed
