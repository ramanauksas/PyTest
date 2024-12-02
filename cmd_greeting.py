import sys
args = sys.argv
print(args)


def say_good_morning(name, surname):
    print(f"Good morning, {name} {surname}!")

def say_good_afternoon(name, surname):
    print(f"Good afternoon, {name} {surname}!")

def say_good_evening(name, surname):
    print(f"Good evening, {name} {surname}!")

def say_good_night(name, surname):
    print(f"Good night, {name} {surname}!")


def main():
    name = args[1]
    surname = args[2]
    hour = int(args[3])
    if hour>=6 and hour<12:
        say_good_morning(name, surname)
    if hour>=12 and hour<18:
        say_good_afternoon(name, surname)
    if hour>=18 and hour<24:
        say_good_evening(name, surname)
    if hour>=0 and hour<6:
        say_good_night(name, surname)

if __name__ == '__main__':
    main()

