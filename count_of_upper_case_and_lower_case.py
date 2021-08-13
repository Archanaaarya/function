def find_case(string):
    upper_case=0
    lower_case=0
    for case in string:
        if case.isupper():
            upper_case=upper_case+1
        elif case.islower():
            lower_case=lower_case+1
        else:
            pass
    print("upper case count:",upper_case)
    print("lower case count:",lower_case)
find_case("my Life is GooD")
    