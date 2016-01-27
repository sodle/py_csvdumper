# csvdumper

Dump dicts and lists to CSV files or strings, in a similar way to the JSON package.

## Methods

* `dump(list_or_dict, filename, *args, **kwargs)`: Dump the list or dictionary to a CSV file specified by the filename. Extra arguments are passed to the constructor of the underlying csv.DictWriter.
* `dumps(list_or_dict, *args, **kwargs)`: Dump the list or dictionary to a string in CSV format, then return it. Extra arguments are passed to the constructor of the underlying csv.DictWriter.