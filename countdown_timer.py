import time

class CountdownTimer:
    def __init__(self, minutes):
        self.minutes = minutes
        self.seconds = minutes * 60  # Convert minutes to seconds

    def start(self):
        print(f"Starting countdown for {self.minutes} minutes...")
        while self.seconds:
            mins, secs = divmod(self.seconds, 60)  # Convert seconds into minutes and seconds
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')  # Print the timer in place to update it every second
            time.sleep(1)
            self.seconds -= 1
        
        print("Time's up! 🚨")

def main():
    try:
        minutes = int(input("Enter time in minutes: "))
        timer = CountdownTimer(minutes)
        timer.start()
    except ValueError:
        print("Please enter a valid number for minutes.")

if __name__ == "__main__":
    main()
