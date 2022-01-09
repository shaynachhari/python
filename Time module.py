import time

watch = time.time()

# i = 0
# while i < 10:
#     print(i)
#     time.sleep(2)
#     i +1
#
# total_time = time.time()
# print(total_time - watch)

#localtime = time.asctime(time.localtime(time.time()))
print( "-------------localtime-----------------" )
print(time.asctime(time.localtime(time.time())))




####*****************************************
'''
import time
import calendar

watch = time.time()
print("Time -> ",time.asctime(time.localtime(time.time())))

cal = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in cal:
    a = calendar.month(2022,i)
    print("-----------Calendar-------------")

    print(a,end='')
'''