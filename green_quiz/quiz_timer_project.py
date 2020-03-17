import time


def countdown(num):
    try:
        while num:
            mins, secs = divmod(num, 60)
            hour, mins = divmod(mins, 60)
            timer = str(hour).zfill(2) + ':' + str(mins).zfill(2) + ':' + str(secs).zfill(2)
            print('\r'+timer, end="")
            time.sleep(1)
            num -= 1
    except:
        KeyboardInterrupt


print()

num = input('ENTER TIME IN SECONDS\n')
countdown(int(num))
