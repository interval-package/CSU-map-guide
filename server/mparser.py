class parser:
    data = {'result': 'success'}
    tars = None
    params = None

    def __init__(self, path):
        if len(path) <= 1 or "/" not in path:
            return

        tars = path.split('/')
        # parse params
        if "?" in tars[-1]:
            params = tars[-1].split('?')
            tars[-1] = params[0]
            params = params[1].split('&')
            self.params = {}
            for i in params:
                if "=" in i:
                    i = i.split("=")
                    self.params[i[0]] = i[-1]
        self.tars = tars
        pass