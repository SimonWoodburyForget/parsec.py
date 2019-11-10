from parsec import string, none_of, sepBy, many

quoted_char = none_of('"') | string('""').result('"')
quoted = (string('"') >> many(quoted_char) << string('"')).parsecmap(lambda x: "".join(x))
cell = quoted | many(none_of(",\n")).parsecmap(lambda x: "".join(x))
cells = sepBy(cell, string(","))
table = sepBy(cells, string("\n"))
