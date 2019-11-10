from parsec import generate, string, one_of, optional, none_of, sepBy, letter, many, try_choice

quoted_char = none_of('"') | string('""').result('"')
quoted = (string('"') >> many(quoted_char) << string('"')).parsecmap(lambda x: "".join(x))
cell = quoted | many(none_of(",\n")).parsecmap(lambda x: "".join(x))
cells = sepBy(cell, string(","))
table = sepBy(cells, string("\n"))

