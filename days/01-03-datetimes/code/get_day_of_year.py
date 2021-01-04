from datetime import datetime as dt


def main():
    print(f"Today is day {dt.now().strftime('%j').lstrip('0')}")


if __name__ == '__main__':
    main()
