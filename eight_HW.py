# вынесено в начале, т.к. возможны другие какие-либо другие варианты кодировки

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


class DNA:
    def __init__(self, seq):
        self.type = "DNA"
        self.seq_string = seq.upper()
        for i in self.seq_string:
            agct = ["A", "G", "C", "T"]
            if i not in agct:
                raise TypeError(
                    "DNA should contain only AGCT characters"
                )

    def __str__(self):
        return f"DNA sequence: {self.seq_string}"

    def __iter__(self):
        return iter(self.seq_string)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.seq_string == other.seq_string

    def __hash__(self):
        return hash(self.seq_string)

    def reverse_seq(self):
        return self.seq_string[::-1]

    def gc_content(self):
        gc = 0
        if len(self.seq_string) > 0:
            gc += sum(map(self.seq_string.count, ['G', 'C'])) / len(self.seq_string)
        return gc

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


class RNA:
    def __init__(self, seq):
        self.type = "RNA"
        self.seq_string = seq.upper()
        for i in self.seq_string:
            agcu = ["A", "G", "C", "U"]
            if i not in agcu:
                raise TypeError(
                    "RNA should contain only AGCU characters"
                )

    def __str__(self):
        return f"RNA sequence: {self.seq_string}"

    def __iter__(self):
        return iter(self.seq_string)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.seq_string == other.seq_string

    def __hash__(self):
        return hash(self.seq_string)

    def reverse_seq(self):
        return self.seq_string[::-1]

    def gc_content(self):
        gc = 0
        if len(self.seq_string) > 0:
            gc += sum(map(self.seq_string.count, ['G', 'C'])) / len(self.seq_string)
        return gc

    def reverse_complement(self):
        table_rna = self.reverse_seq().maketrans(tables['trans_table_RNA'])
        transcribed_seq = self.seq_string.translate(table_rna)
        return RNA(transcribed_seq)
