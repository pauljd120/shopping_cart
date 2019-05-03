from shopping_cart import to_usd, find_product

def test_to_usd():
    result = to_usd(50)
    assert result == "$50.00"

def test_find_product():
    products = [{"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},]

    index_list = []

    id_index = 2

    index_list.append(id_index)

    running_total = 0

    for each in index_list:
        result = find_product(each, products, running_total)

    assert result == 4.99
