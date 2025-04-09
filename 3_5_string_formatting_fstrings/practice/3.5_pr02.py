# put your python code here
width, depth, height = map(int, input().split())
text_message = 'Габариты: {width_this} x {depth_this} x {height_this}'.format(width_this=str(width), depth_this=str(depth),height_this=str(height))
print(text_message)