# display resolution
try:
    # linux
    from Xlib.display import Display
    screen = Display(':0').screen()
    sys_width = screen.width_in_pixels
    sys_height = screen.height_in_pixels
except:
    try:
        # windows
        from win32api import GetSystemMetrics
        sys_width = GetSystemMetrics(0)
        sys_height = GetSystemMetrics(1)
    except:
        # other os
        sys_width = None
        sys_height = None
        pass

# display resolution
def display():
    return sys_width, sys_height

        