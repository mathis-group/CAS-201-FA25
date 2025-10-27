
def hello(date, name = "Patrick", **kwargs):
    print(f"Hello {name}, today is {date}!")
    if kwargs:
        print(kwargs)

if __name__ == "__main__":
    hello("Oct 27th", "Kevin", classmate = "Can", course = "CAS201")