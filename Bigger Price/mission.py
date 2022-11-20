def bigger_price(limit: int, data: list) -> list:
    sort = sorted(data, key=lambda x: x['price'], reverse=True)
    result = []
    for x in range(limit):
        result.append(sort[x])

    return result








if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "meat", "price": 15},

        {"name": "wine", "price": 138},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [{'name': 'bread', 'price': 10}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'milk', 'price': 25}]) == [{'name': 'wine', 'price': 138}, {'name': 'milk', 'price': 25}]

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
