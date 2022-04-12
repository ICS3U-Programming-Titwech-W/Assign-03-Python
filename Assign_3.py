#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.6. 2022

# program tells student to take the
# exam if they atted 75% or more of theor classes

from colorama import Fore


def main():

    # try catch
    try:
        # string into integer
        classes_held = float(input("How many classes are held?: "))
        classes_attend = float(input("How many classes did you attend?: "))
        print("")

        classes_held = int(classes_held)
        classes_attend = int(classes_attend)

        percent = (classes_attend/classes_held)*100

        # Percent is hight than 75
        if percent >= 75:
            print(Fore.CYAN + "You can take the final exam")

        else:
            print(Fore.MAGENTA + "you can’t take the final exam.")
            print(Fore.MAGENTA + "you’ve only attended {}% of your classes."
                                 .format(percent))
            print("")

    except Exception:
        # user did not enter a number
        print(Fore.MAGENTA + "Please enter your number of classes")
        print(Fore.MAGENTA + "you have attended and held classes")

    finally:
        print(Fore.YELLOW + "Thank you!")


if __name__ == "__main__":
    main()
