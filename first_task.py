import argparse

def from_file(func):
    def wrapper():
        with open(file, 'r') as f:
            value, *data = [line.rstrip('\n').split(' ') for line in f]
        func(data)
    return wrapper

def from_input(decorator):
    def new_decorator(func):
        decorated = decorator(func)
        def wrapper():
            if decorator.enabled:
                return decorated()
            else:
                print('Enter your data')
                data = [input().split(' ') for i in range(int(input()))]
                func(data)
        return wrapper
    decorator.enabled = True
    return new_decorator

@from_input(from_file)
def main(data):
    data.sort(key=lambda x: x[-1])
    [print(
        ' '.join(['Г-жа',*i[:2]]) if i[2] == 'Ж' else ' '.join(['Г-н',*i[:2]])
    ) for i in data]

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
