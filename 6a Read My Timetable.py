#Read My Timetable

#----------------------------------------
def readfile(day):

    filename=day+".txt"
    channel = open(filename,"r+")
    lesson=channel.readlines()

    channel.close()
    return lesson
#----------------------------------------


day=input("Day of week")

lesson=readfile(day)
print(lesson)