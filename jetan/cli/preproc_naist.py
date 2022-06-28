from pathlib import Path
from argparse import ArgumentParser
import xml.etree.ElementTree as ET

def add_goyo_text(goyo, pair):
    if goyo.text is not None:
        pair.src += goyo.text.strip()


def make_goyo_attrib(goyo):
    attrs = [
        attr
        for attr
        in goyo.attrib
        if attr.startswith('c')]
    attrs.sort()
    return attrs


def add_goyo_attrib_one_to_one(goyo, pair):
    pair.trgs = [
        trg + goyo.attrib['crr'].strip()
        for trg
        in pair.trgs]


def add_goyo_attrib_one_to_many(goyo, pair, attrs):
    pair.trgs = [
        trg + goyo.attrib[attr].strip()
        for trg
        in pair.trgs
        for attr
        in attrs]


def add_goyo_attrib_many_to_many(goyo, pair, attrs):
    pair.trgs = [
        trg + goyo.attrib[attr].strip()
        for trg, attr
        in zip(pair.trgs, attrs)]


def add_goyo_attrib(goyo, pair):
    attrs = make_goyo_attrib(goyo)

    if len(attrs) == 1:
        add_goyo_attrib_one_to_one(goyo, pair)
    elif len(pair.trgs) == 1:
        add_goyo_attrib_one_to_many(goyo, pair, attrs)
    elif len(pair.trgs) == len(attrs):
        add_goyo_attrib_many_to_many(goyo, pair, attrs)
    else:
        assert False


def add_goyo_tail(goyo, pair):
    if goyo.tail is not None:
        tail = goyo.tail.strip()
        pair.src += tail
        pair.trgs = [
            trg + tail
            for trg
            in pair.trgs]


class Pair:

    def __init__(self):
        self.src = ''
        self.trgs = ['']

    def add_text(self, text):
        text = text.strip()
        self.src += text
        self.trgs = [trg + text for trg in self.trgs]


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('base')
    return parser.parse_args()


def get_xml_path_list(base_path):
    base = Path(base_path).resolve()
    xml_list = list(base.glob('*/*.xml'))
    xml_list.sort()
    return xml_list


def xml_to_sent_list(xml_path):
    xml = ET.parse(xml_path)
    root = xml.getroot()

    text = [
        child
        for child
        in root
        if child.tag == 'text']

    assert len(text) == 1
    text = text[0]

    sents = [
        sent
        for para
        in text
        for sent
        in para]

    return sents


def make_pair(pair, sent):
    if sent.text is not None:
        pair.add_text(sent.text)

    for goyo in sent:
        add_goyo_text(goyo, pair)
        add_goyo_attrib(goyo, pair)
        add_goyo_tail(goyo, pair)


def show_pair(pair):
    lst = [pair.src] + pair.trgs
    line = '\t'.join(lst)
    print(line)


def main():
    args = parse_args()

    xml_list = get_xml_path_list(args.base)

    sent_list = [
        sent
        for xml
        in xml_list
        for sent
        in xml_to_sent_list(xml)]

    for sent in sent_list:
        pair = Pair()
        make_pair(pair, sent)
        show_pair(pair)

