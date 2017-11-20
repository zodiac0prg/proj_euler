
days = ["Mon", "Tue", "Wed", "Thu" , "Fri", "Sat", "Sun"];
months = { "Jan" : 31,
           "Feb" : 28,
           "Mar" : 31,
           "Apr" : 30,
           "May" : 31,
           "Jun" : 30,
           "Jul" : 31,
           "Aug" : 31,
           "Sep" : 30,
           "Oct" : 31,
           "Nov" : 30,
           "Dec" : 31 }

def is_leap_year(year):
    if (year % 4 != 0):
        return False
    
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True
    else:
        if (year % 4 == 0):
            return True

    return False

def update_cur_day (cur_day , day_count):
    count = 1
    i = days.index(cur_day)
    while True:
        #print days[i]
        if days[i] == "Sun":            
            #print i, count
            count += 1
            if (count == day_count):                
                i = 0
                #print "Here1"
                break
            i = 0
            #print days[i]
        
        i += 1
        count += 1        
       
        #print count    
        if (count == day_count):
            #print "Here2"
            break

    if (days[i] == "Sun"):
        return days[0]
    else:
        return days[i + 1]

def update_cur_month (cur_month):
    if (cur_month == "Jan"):
        return "Feb"
    elif (cur_month == "Feb"):
        return "Mar"
    elif (cur_month == "Mar"):
        return "Apr"
    elif (cur_month == "Apr"):
        return "May"
    elif (cur_month == "May"):
        return "Jun"
    elif (cur_month == "Jun"):
        return "Jul"
    elif (cur_month == "Jul"):
        return "Aug"
    elif (cur_month == "Aug"):
        return "Sep"
    elif (cur_month == "Sep"):
        return "Oct"
    elif (cur_month == "Oct"):
        return "Nov"
    elif (cur_month == "Nov"):
        return "Dec"
    elif (cur_month == "Dec"):
        return "Jan"

cur_year = 1901
cur_day = days[1]
day_count = 0
cur_month = "Jan"
end_year = 2001
sum_sun = 0


while True:
    for month_count in range(12):
        day_count = months[cur_month]
        if (cur_month == "Feb" and is_leap_year(cur_year)):
            day_count += 1

        if (cur_day == "Sun"):
            sum_sun += 1
       
        #print cur_day , day_count
        cur_day = update_cur_day(cur_day, day_count)
        cur_month = update_cur_month (cur_month)
        
    cur_year += 1
    if (cur_year == end_year):
        break

print sum_sun


#print update_cur_day("Sat", 31)
