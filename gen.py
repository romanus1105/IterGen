def flat_generator(iterable):
    for item in iterable:
        if type(item) == list:
            yield from flat_generator(item)
        else:
            yield item

def main():
    nested_list = [
        ['aa', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)

if __name__ == "__main__":
   main()