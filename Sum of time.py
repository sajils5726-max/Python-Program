class Time:
    def __init__(self, hour, minutes, seconds):
        
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

   
    def show(self):
        print(f"{self.__hour:02d}:{self.__minutes:02d}:{self.__seconds:02d}")

  
    def __add__(self, other):
       
        seconds = self.__seconds + other.__seconds
        minutes = self.__minutes + other.__minutes
        hour = self.__hour + other.__hour

        
        if seconds >= 60:
            minutes += seconds //60
            seconds = seconds %60

        if minutes >= 60:
            hour += minutes //60
            minutes = minutes %60

        return Time(hour, minutes, seconds)



t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)

print("Time 1:")
t1.show()

print("Time 2:")
t2.show()

t3 = t1 + t2  
print("Sum of Time:")
t3.show()