from os import path


def response(filename, params={}):
    try:
        if not path.exists("template"):
            raise Exception('Template folder doesn\'t exist')
        file = open('template/' + filename + '.html', 'r')
        data = file.read()
    except:
        print('Error in Loading/Reading file ' + filename)
        return b'null'
    for key, val in params.items():
        data = data.replace('%' + key + '%', val)
    return str.encode(data)
