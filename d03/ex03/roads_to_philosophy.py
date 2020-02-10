import requests, sys
from bs4 import BeautifulSoup

def road(param, elems):
    param = param.replace(" ", "_")
    s = requests.Session()
    elems.append(param)
    url = 'https://en.wikipedia.org/wiki/'
    if url + param == 'https://en.wikipedia.org/wiki/Philosophy':
        for q in elems:
            q = q.replace("_", " ")
            print(q)
        print("%s roads from %s" %(len(elems), elems[0]))
        return 0
    r = s.get(url=url + param)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    res = soup.find_all('p')
    for p in res:
        pos = p.find_all('a')
        for f in pos:
            if f.has_attr("title"):
                fos = f['title']
                hos = f["href"]
                if hos.startswith("/wiki/File:") == False and not hos in elems:
                    return road(hos.replace("/wiki/", ""), elems)

def go():
    if len(sys.argv) != 2:
        print("Something wrong")
    else:
        param = sys.argv[1]
        param = param.replace(" ", "_")
        elems = []
        road(param, elems)

if __name__ == '__main__':
    go()