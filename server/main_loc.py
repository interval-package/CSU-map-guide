import json
import urllib3
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json
import pandas as pd
sql = sqlite3.connect("./info.db")
from mparser import parser

host = ('localhost', 8080)
# host = ('192.168.43.39', 8080)

img = {"url": "http://zaterval.top/upload/2022/09/logo.png"}


def get_all():
    res = []
    cur = sql.execute("select * from school_locs")
    cols = [i[0] for i in cur.description]
    for tar in cur.fetchall():
        temp = {}
        for i, j in zip(cols, tar):
            temp[i] = j
        res.append(temp)
    return res


class path_parser(parser):

    def __init__(self, path):
        super().__init__(path)

    def get_res(self) -> bytes:

        data = self.data

        print(self.tars)

        if self.tars[1] == "banner":
            if self.tars[2] == "1":
                data = {
                    "item": [{
                        "id": 1,
                        "image": img,
                    }]
                }
                pass
            elif self.tars[2] == "2":
                data = {
                    "detail": {
                        "name": "name temp",
                        "name_eng": "csu",
                        "detail": "detail text here"
                    }
                }
                pass
            pass

        elif self.tars[1] == "detail":
            if self.tars[2] == "2":
                data = {
                    "detail": {
                        "name": "中南大学好好的",
                        "name_eng": "csu",
                        "detail": "没有详细内容，就随便吧"
                    }
                }
                pass
            pass

        elif self.tars[1] == "location":
            if self.tars[2] == "list":
                _all = get_all()
                data = []
                for i, tar in enumerate(_all):
                    data.append({
                        "id": i+1,
                        "name": tar["loc_name"],
                        "image": {"url": tar["img_url"]},
                        "coordinate_items": {
                            "id": i+1,
                            "lat": tar["lat"],
                            "lon": tar["lon"],
                        },
                        "lat": tar["lat"],
                        "lon": tar["lon"],
                    })
                pass
            elif self.tars[2].isdigit():
                idx = int(self.tars[2])
                _all = get_all()
                tar = _all[idx-1]
                _data = {
                    "image": {"url": tar["img_url"]},
                    "name": tar["loc_name"],
                    "detail": tar["detail"],
                    "id": idx,
                    "lat": tar["lat"],
                    "lon": tar["lon"],
                }
                data = _data.copy()
                data["coordinate_items"] = _data
                pass
            pass

        elif self.tars[1] == "list":

            _all = get_all()
            data = []
            for i, tar in enumerate(_all):
                data.append({
                    "items": [{"id": i+1}],
                    "id": i+1,
                    "name": tar["loc_name"],
                    "image": {"url": tar["img_url"]},
                    "coordinate_items": {
                        "id": i+1,
                        "lat": tar["lat"],
                        "lon": tar["lon"],
                    },
                    "lat": tar["lat"],
                    "lon": tar["lon"],
                })
            pass

        elif self.tars[1] == "sort":
            _all = get_all()
            data = []
            for i, tar in enumerate(_all):
                data.append({
                    "items": [{"id": i+1}],
                    "id": i+1,
                    "name": tar["loc_name"],
                    "image": {"url": tar["img_url"]},
                    "coordinate_items": {
                        "id": i+1,
                        "lat": tar["lat"],
                        "lon": tar["lon"],
                    },
                    "lat": tar["lat"],
                    "lon": tar["lon"],
                })
            pass

        elif self.tars[1] == "search":
            pass

        return json.dumps(data).encode()

    pass


class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        print("get the path:", self.path)

        obj = path_parser(self.path)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(obj.get_res())

    def do_POST(self):
        _data = self.rfile.read(int(self.headers['content-length']))
        print('headers', self.headers)
        print("do post:", self.path, self.client_address, _data)


if __name__ == '__main__':
    server = HTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
