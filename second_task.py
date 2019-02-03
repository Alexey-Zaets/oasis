import argparse


def from_file(func):
    def wrapper():
        with open(file, 'r') as f:
            data = []
            request = []
            gen = (line.rstrip('\n') for line in f)
            try:
                value = int(next(gen))
                while value:
                    data.append(next(gen))
                    value -= 1
                value = int(next(gen))
                while value:
                    request.append(next(gen))
                    value -= 1
            except StopIteration:
                pass
        func(data, request)
    return wrapper

def from_input(decorator):
    def new_decorator(func):
        decorated = decorator(func)
        def wrapper():
            if decorator.enabled:
                return decorated()
            else:
                print('Enter your data')
                data = [input() for i in range(int(input()))]
                request = [input() for i in range(int(input()))]
                func(data, request)
        return wrapper
    decorator.enabled = True
    return new_decorator

@from_input(from_file)
def main(x, y):
    [print(x.count(i)) for i in y]

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', help='path to file with data')
args = parser.parse_args()
file = args.file if args.file else None


if __name__ == '__main__':
    if file is not None:
        main()
    else:
        from_file.enabled = False
        main()
