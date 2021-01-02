light = input.light_level()

if input.light_level() < 5:
    light.set_all(color.rgb(0, 255, 255))
    