# put your python code here
X, Y = map(int, input().split())
number_of_blue_pens = X
number_of_green_pens = Y
number_of_black_pens = number_of_blue_pens*2
number_of_red_pens = number_of_green_pens*4
number_of_pens = number_of_blue_pens+number_of_green_pens+number_of_black_pens+number_of_red_pens
print(number_of_pens)