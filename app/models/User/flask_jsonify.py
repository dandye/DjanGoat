import json as _json


def dumps(obj, **kwargs):
    encoding = kwargs.pop("encoding", None)
    rv = _json.dumps(obj, **kwargs)

    if isinstance(rv, str):
        return rv.encode(encoding)

    return rv


def flask_jsonify(*args, **kwargs):
    indent = 2
    separators = (", ", ": ")

    if args and kwargs:
        raise TypeError("jsonify() behavior undefined when passed both args and kwargs")
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs

    return str(dumps(data, indent=indent, separators=separators))