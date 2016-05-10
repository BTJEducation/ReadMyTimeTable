#Read My Timetable

def readfile(day):

    filename=day+".txt"
    channel = open(filename,"r+")
    lesson=channel.readlines()

    channel.close()
    return lesson
#----------------------------------------

day=input("Day of week")

lesson=readfile(day)

print("Day - ",day,"\n" )
lesson_num=1

for i in lesson:
    (subject, teacher)=(i.split(","))
    print("Lesson {} - {} {}".format(lesson_num,subject, teacher))
    lesson_num +=1
