from pyfiglet import figlet_format


def print_arg(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)


print_arg('Python is awesome')
