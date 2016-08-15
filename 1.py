import re
from urllib import request
from argparse import ArgumentParser
from sys import exit


class ThreadDownloader:
    def __init__(self, lnk):
        self.page = request.urlopen(lnk).read().decode("utf-8")
        self.dwn_link = lnk.replace("res", "src").replace(".html", "/")
        self.pics = self.make_list_of_pics()

    def make_list_of_pics(self):
        pic_re = re.compile('\d+\.jpg')
        return set(re.findall(pic_re, self.page))

    def start(self):
        for pic in self.pics:
            print("Downloading: " + self.dwn_link + pic)
            t = request.urlopen(self.dwn_link + pic).read()
            u = open(pic, "wb")
            u.write(t)
            u.close()


def mad():
    print('R U MAD?')
    exit()


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument("-t", "--thread", type=int, help="Num of thread")
    p.add_argument("-l", "--link", type=str, help="Link to thread")
    p.add_argument("path", type=str, help="Path to save")
    args = p.parse_args()
    link = "https://2ch.hk/b"
    if args.thread and args.link:
        mad()
    elif args.thread:
        link = "https://2ch.hk/b/res/" + args.thread + ".html"
    elif args.link:
        if args.link.startswith("https://2ch.hk/"):
            link = args.link
        else:
            mad()
    ThreadDownloader(link).start()
