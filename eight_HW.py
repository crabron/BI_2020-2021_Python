class NAcid(object):
    def __init__(self, seq):
        self.__seq_string = seq
        self.__seq = tuple(seq)
        self.trans_table_DNA = self.__seq_string.maketrans(
            {
                'A': 'T',
                'T': 'A',
                'C': 'G',
                'G': 'C'
            }
        )
        self.trans_table_RNA = self.__seq_string.maketrans(
            {
                'A': 'U',
                'U': 'A',
                'C': 'G',
                'G': 'C'
            }
        )
        self.trans_table_DNA_RNA = self.__seq_string.maketrans(
            {
                'A': 'U',
                'T': 'A',
                'C': 'G',
                'G': 'C'
            }
        )

    def __str__(self):
        return f"{self.__seq_string}"

    def __iter__(self):
        self.__n = 0
        return iter(self.__seq_string)

    def __next__(self):
        if self.__n + 1 < len(self.__seq_string):
            self.__n += 1
            return self.__seq_string[self.__n]
        else:
            raise StopIteration

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__seq_string == other.__seq_string

    def __hash__(self):
        return hash(self.__seq_string)

    def transcribe(self):
        if isinstance(self, DNA):
            transcripted_seq = self.__seq_string.translate(self.trans_table_DNA_RNA)
            return RNA(transcripted_seq)
            # return RNA(translated_dna)
        else:
            print("cant translate notDNA")

    def reverse_compliment(self):
        if isinstance(self, DNA):
            transcripted_seq = self.__seq_string.translate(trans_table)
            return RNA(transcripted_seq)
            # return RNA(translated_dna)
        if isinstance(self, RNA):
            print("cant translate notDNA")


class DNA(NAcid):
    pass

    def __str__(self):
        return "DNA sequence: " + super().__str__()


class RNA(NAcid):
    pass

    def __str__(self):
        return "RNA sequence: " + super().__str__()


a = DNA('AGGAA')
b = RNA('AGAA')

print(a.transcribe())
# print(b.translate())

print(a)
