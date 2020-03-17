import time


def countdown(num):
    while num:
        mins, secs = divmod(num, 60)
        hour, mins = divmod(mins, 60)
        timer = str(hour).zfill(2) + ':' + str(mins).zfill(2) + ':' + str(secs).zfill(2)
        print(timer + '\r', end="")
        time.sleep(1)
        num -= 1


print()

num = input('ENTER TIME IN SECONDS\n')
countdown(int(num))
