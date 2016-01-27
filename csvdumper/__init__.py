import csv
import StringIO


def _multi_union(*operands):
    union = set()
    for operand in operands:
        union = set(union) | set(operand)
    return union


def _dump_dict(dictionary, file_obj, *args, **kwargs):
    fieldnames = dictionary.keys()
    writer = csv.DictWriter(file_obj, fieldnames, *args, **kwargs)

    writer.writeheader()
    writer.writerow(dictionary)


def _dump_list(list_in, file_obj, *args, **kwargs):
    fieldsets = [d.keys() for d in list_in]
    fieldnames = _multi_union(*fieldsets)
    writer = csv.DictWriter(file_obj, fieldnames, *args, **kwargs)

    writer.writeheader()
    writer.writerows(list_in)


def _dump(obj_in, file_obj, *args, **kwargs):
    if type(obj_in) == list:
        _dump_list(obj_in, file_obj, *args, **kwargs)
    elif type(obj_in) == dict:
        _dump_dict(obj_in, file_obj, *args, **kwargs)
    else:
        raise ValueError('obj_in is not list or dictionary')


def dump(obj_in, filename, *args, **kwargs):
    with open(filename, 'w') as csv_file:
        _dump(obj_in, csv_file, *args, **kwargs)


def dumps(obj_in, *args, **kwargs):
    out_writer = StringIO.StringIO()
    _dump(obj_in, out_writer, *args, **kwargs)
    output = out_writer.getvalue()
    out_writer.close()
    return output
