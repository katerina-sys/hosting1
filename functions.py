def filter_query(param, data):
    return list(filter(lambda x: param in x, data))


def map_query(param, data):
    column = int(param)
    return list(map(lambda x: x.split(' ')[column], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sort_query(param, data):
    reverse = False if param == 'acs' else True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    limit = int(param)
    return list(data)[:limit]