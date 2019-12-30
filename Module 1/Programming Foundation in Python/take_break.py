# step 1 : Wait for two hours
# step 2 : Open your browser
# step 3 : reapeat Step 1 and 2, 3 times

import time
import webbrowser

count = 1
while (count <= 3):
    # makes the program wait for 10 seconds
    time.sleep(10)
    # prompt the web browser
    webbrowser.open('https://www.youtube.com')
    # Increment
    count = count + 1