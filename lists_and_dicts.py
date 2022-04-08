def run():
    my_list = [1, "Hello", True, 4.5]
    my_dyct = {"firstname": "Juan",
                "lastname":"Bueno"}

    super_list = [
        {"firstname": "Juan", "lastname":"Bueno"},
        {"firstname": "Cami", "lastname":"Bueno"},
        {"firstname": "Lele", "lastname":"Bueno"},
        {"firstname": "Dani", "lastname":"Bueno"}
    ]

    super_dict={
        "narutal_nums": [ 1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for items_dicts in super_list:
        print(items_dicts['firstname'], ' ', items_dicts['lastname'])

    for key, value in super_dict.items():
        print(key, '-', value)

if __name__ == '__main__':
    run()