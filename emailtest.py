import time

time_string = '2016-06-03T23:14:56+01:00'

tuple_time = time.strptime(time_string[0:19], "%Y-%m-%dT%H:%M:%S")

print (str(tuple_time[3]) +':'+ str(tuple_time[4]))