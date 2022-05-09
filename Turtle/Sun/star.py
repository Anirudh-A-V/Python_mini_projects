from turtle import *
color('red', 'yellow')
begin_fill()
goto(-100,0)

for i in range(36):
    forward(200)
    left(110)
    # if abs(pos()) < 1:
        # break
end_fill()
done()