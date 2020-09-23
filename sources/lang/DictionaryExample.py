def zip_two_lists_to_dictionary():
    key = ["Facebook", "Tesla", "Apple", "Amazon", "Google"]
    value = ["FB", "TSLA", "AAPL", "AMZN", "GOOG"]
    stock = dict(zip(key, value))
    for key, value in enumerate(stock, start=1):
        print(f'key: {key} value: {value}')


if __name__ == "__main__":
    zip_two_lists_to_dictionary()
