from pathlib import Path

import httpx
from lxml import etree

from python_project.tools import consts


def get_latest_version():
    golang_html = consts.cache_dir.joinpath("golang.html")
    if golang_html.exists():
        with open(golang_html, "r", encoding="utf-8") as fr:
            html_txt = fr.read()
    else:
        r = httpx.get(url="https://golang.google.cn/dl/")
        with open(golang_html, "w", encoding="utf-8") as fw:
            html_txt = r.text
            fw.write(html_txt)
    html = etree.HTML(html_txt)
    v_list = html.xpath('//div[@class="expanded"]/h2/text()')
    versions = [
        tuple(map(int, v.strip().removeprefix("go").removesuffix(" ▾").split(".")))
        for v in v_list
        if "rc" not in v and "beta" not in v
    ]
    return max(versions)


def get_all_versions():
    golang_html = consts.cache_dir.joinpath("golang.html")
    if golang_html.exists():
        with open(golang_html, "r", encoding="utf-8") as fr:
            html_txt = fr.read()
    else:
        r = httpx.get(url="https://golang.google.cn/dl/")
        with open(golang_html, "w", encoding="utf-8") as fw:
            html_txt = r.text
            fw.write(html_txt)
    html = etree.HTML(html_txt)
    v_list = html.xpath('//div[@class="expanded"]/h2/text()')
    versions = [v.strip().removeprefix("go").removesuffix(" ▾") for v in v_list]
    return versions
