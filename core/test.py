import gevent
import requests
import time


def get_res(url):
    res = requests.get(url)
    print(res.content.decode('utf-8'))


if __name__ == '__main__':
    g_lista = []
    start_time = time.time()
    for i in range(50):
        g = gevent.spawn(get_res, 'http://www.163.com')
        g_lista.append(g)
        print(i, flush=True)
    print(len(g_lista))
    [a.join() for a in g_lista]
    end_time = time.time() - start_time
    print(end_time)