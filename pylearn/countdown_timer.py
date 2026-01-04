import time

my_time = int(input("Enter the time in seconds: "))
for i in range(my_time, 0, -1):
    secs = i%60
    mins = (i//60)%60
    hrs = (i//3600)
    print(f"Time left: {hrs:02d}:{mins:02d}:{secs:02d}")
    time.sleep(1)   
print("Time up!")
