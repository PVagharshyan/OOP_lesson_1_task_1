import Student

if __name__ == "__main__":
    s1 = Student.Student("Poghos Poghosyan",24)
    print(s1.get_id())
    print(s1.get_name())
    print(s1.get_age())
    s1.set_name("Petros Petrosyan")
    s1.set_age(15)
    print(s1.get_id())
    print(s1.get_name())
    print(s1.get_age())



