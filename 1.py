import re
from urllib import request
from argparse import ArgumentParser
from sys import exit
import os


class ThreadDownloader:
    def __init__(self, lnk, path):
        try:
            self.page = request.urlopen(lnk).read().decode("utf-8")
        except request.HTTPError as e:
            print(str(e))
            exit()
        self.dwn_link = lnk.replace("res", "src").replace(".html", "/")
        self.pics = self.make_list_of_pics()
        self.path = path

    def make_list_of_pics(self):
        pic_re = re.compile('\d+\.jpg')
        return set(re.findall(pic_re, self.page))

    def start(self):
        for pic in self.pics:
            print("Downloading: " + self.dwn_link + pic)
            t = request.urlopen(self.dwn_link + pic).read()
            save_path = self.path + '/' + pic
            u = open(save_path, "wb")
            print("Saving: " + save_path)
            u.write(t)
            u.close()


def mad():
    print('Используйте только один из ключей -t или -l')
    exit()


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument("-t", "--thread", type=int, help="Num of thread in /b")
    p.add_argument("-l", "--link", type=str, help="Link to thread")
    p.add_argument("-p", "--path", type=str, help="Path to save")
    args = p.parse_args()
    link = "https://2ch.hk/b"
    path = "."
    if args.path:
        path = args.path
    if not os.path.isdir(path):
        print("Неверный путь")
        exit()
    if bool(args.thread) == bool(args.link):
        mad()
    elif args.thread:
        link = "https://2ch.hk/b/res/" + str(args.thread) + ".html"
    elif args.link:
        if args.link.startswith("https://2ch.hk/"):
            link = args.link
        else:
            mad()
    ThreadDownloader(link, path).start()
