#There is no compelling reason for preferring recursion over loops. As, more we approach towarsd more complex example, consider how to draw an ruler
#markings. For each inch, we place a tick with a numeric label. We denote the length of the tick designated a whole inch as the major tick length.

def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length(followed by the optional label)"""
    line = '-' * tick_length
    if tick_length:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:                  #stop when length drops to 0
        draw_interval(center_length - 1)   #recursively draw top ticks
        draw_line(center_length)           #draw center tick
        draw_interval(center_length - 1)   #recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')           #draw inch 0 line
    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)    #draw interior ticls for inch
        draw_line(major_length, str(j))    #draw inch j line and label