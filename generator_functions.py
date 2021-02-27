from itertools import product
from Bio import SeqIO


def generate(a):
    res = []
    for a in range(1, a + 1):
        yield from [''.join(i) for i in product('ATGC', repeat=a)]


def dumb_translater(path, table="Standart"):
    for fasta in SeqIO.parse(path, "fasta"):
        yield from ["M" + str(i.translate(table=table, to_stop=True)) for i in fasta.seq.split("ATG")]
