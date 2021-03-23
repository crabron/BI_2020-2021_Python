tables = dict(trans_table_DNA={
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}, trans_table_RNA={
    'A': 'U',
    'U': 'A',
    'C': 'G',
    'G': 'C'
}, trans_table_DNA_RNA={
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
})


class NAcid(object):
    def __init__(self, seq) -> object:
        self.seq_string = seq
        self.seq = tuple(seq)

    def __str__(self):
        return f"{self.seq_string}"

    def __iter__(self):
        self.__n = 0
        return iter(self.seq_string)

    def __next__(self):
        if self.__n + 1 < len(self.seq_string):
            self.__n += 1
            return self.seq_string[self.__n]
        else:
            raise StopIteration

    def __eq__(self, other):
        if type(other) is type(self):
            return self.seq_string == other.__seq_string

    def __hash__(self):
        return hash(self.seq_string)

    def reverse_seq(self):
        return self.seq_string[::-1]


class DNA(NAcid):
    pass

    def __str__(self):
        return "DNA sequence: " + super().__str__()

    def transcribe(self):
        if isinstance(self, DNA):
            table_dna_rna = self.seq_string.maketrans(tables['trans_table_DNA_RNA'])
            transcribed_seq = self.seq_string.translate(table_dna_rna)
            return RNA(transcribed_seq)
        else:
            print("cant translate notDNA")

    def reverse_complement(self):
        table_dna = self.reverse_seq().maketrans(tables['trans_table_DNA'])
        transcribed_seq = self.seq_string.translate(table_dna)
        return DNA(transcribed_seq)


class RNA(NAcid):
    pass

    def __str__(self):
        return "RNA sequence: " + super().__str__()

    @property
    def reverse_complement(self):
        table_rna = self.reverse_seq().maketrans(tables['trans_table_RNA'])
        transcribed_seq = self.seq_string.translate(table_rna)
        return RNA(transcribed_seq)
