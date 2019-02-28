from turtle import *
speed ()
shape ()

color("red","white")

begin_fill()
for i in range (4):
    forward (130)
    left (90)
left (120)      
for j in range (5):
     forward (130)
     right (60)

end_fill ()

color ("blue")
begin_fill

# Tam giác:
right (60)
forward (125)
left(118)
forward (126)

# Tứ giác:
right (130)
forward (130)
right (80)
forward (120)
right (55)
forward (120)
right (82)
forward (130)

end_fill

mainloop ()