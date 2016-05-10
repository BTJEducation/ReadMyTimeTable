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

print("Day - ",day,"\n")

for i in lesson:
    (subject, teacher)=(i.split(","))
    print("Subject {}, Teacher {}".format(subject, teacher))

