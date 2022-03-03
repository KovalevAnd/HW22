
csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = read(csv)
    data = sort(data)
    data = filter(data)
    return data


def read(line):
    data = []
    for i in line.split('\n'):
        name, age = i.split(';')
        data.append([name, int(age)])
    return data


def sort(data):
    return sorted(data, key=lambda x: int(x[1]))


def filter(data):
    return [x for x in data if int(x[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
