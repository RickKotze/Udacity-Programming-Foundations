import webbrowser
import time

total_breaks = 3
break_count= 0
seconds=1

print ("This program started on "+time.ctime())
while (total_breaks>break_count):
   time.sleep(seconds)
   print ("the video started playing at " +time.ctime()) 
   webbrowser.open("https://www.youtube.com/watch?v=12J6SEGVydk")
   break_count=break_count+1
   
