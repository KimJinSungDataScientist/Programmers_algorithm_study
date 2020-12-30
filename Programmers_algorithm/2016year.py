a=5
b=24

mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
tot_day = 0

for i in range(a-1):
    tot_day += mon[i]

tot_day += b

if tot_day%7==0:
    answer = "THU"
elif tot_day%7==1:
    answer = "FRI"
elif tot_day%7==2:
    answer = "SAT"
elif tot_day%7==3:
    answer = "SUN"
elif tot_day%7==4:
    answer = "MON"
elif tot_day%7==5:
    answer = "TUE"
elif tot_day%7==6:
    answer = "WED"

print(answer)