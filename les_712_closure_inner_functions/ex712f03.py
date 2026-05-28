def strip_string(dtrip_chars=' '):
    def do_strip(string):
        return string.strip(dtrip_chars)

    return do_strip


c1 = strip_string()
c2 = strip_string('_ ')
print(c1('    dfgdfgdfg_____'))
print(c2('    dfgdfgdfg_____'))