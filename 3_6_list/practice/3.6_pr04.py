# put your python code here
marks = list(map(int, input().split()))
marks_sum = sum(marks)
marks_length = len(marks)
marks_avg = marks_sum / marks_length
print(round(marks_avg, 1))