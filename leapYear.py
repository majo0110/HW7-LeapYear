def LeapYear(year):
    if ( year % 400 == 0):
        print(year, "is a leap year.")
    elif (year % 100 == 0 ):
        print(year, "is not a leap year.")
    elif (year % 4 == 0):
        print(year, "is a leap year.")


if __name__ == "__main__":
    main()
