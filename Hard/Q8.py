def decode(a):
    a_split = a.split('0')
    a_split = [x for x in a_split if x]
    print(a_split)
    a_dict = {}
    a_dict["first_name"] = a_split[0]
    a_dict["last_name"] = a_split[1]
    a_dict["id"] = a_split[2]

    print(a_dict)





a = "Robert000Kardashian000123"

decode(a)