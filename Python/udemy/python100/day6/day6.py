# def my_func():
#   print("Hellow")
#   print("Bye")

# my_func()


def turn_right():
  turn_left()
  turn_left()
  turn_left()


while front_is_clear():
  move()
turn_left()

while not at_goal():
  while wall_on_right():
    if front_is_clear():
      move()
    else:
      turn_left()
  if at_goal():
    break
  turn_right()
  move()
  if at_goal():
    break
