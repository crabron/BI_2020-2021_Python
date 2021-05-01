import unittest
from eight_HW import DNA, RNA


class DnaRnaTest(unittest.TestCase):
    dna_regular = DNA('AAAATTTTGGCCAAAA')
    dna_lowcase = DNA('aaaattttggccaaaa')
    dna_empty = DNA('')
    rna_regular = RNA('AAAAUUUUGGCCaaaa')
    rna_lowcase = RNA('aaaauuuuggccaaaa')
    rna_empty = RNA('')

    def test_type_self(self):
        self.assertEqual(self.dna_regular.type, "DNA")
        self.assertEqual(self.dna_lowcase.type, "DNA")
        self.assertEqual(self.dna_empty.type, "DNA")
        self.assertEqual(self.rna_regular.type, "RNA")
        self.assertEqual(self.rna_lowcase.type, "RNA")
        self.assertEqual(self.rna_empty.type, "RNA")

    def test_zero(self):
        self.assertEqual(len(self.dna_empty.seq_string), 0)
        self.assertEqual(len(self.rna_empty.seq_string), 0)

    def test_gc(self):
        self.assertEqual(self.dna_regular.gc_content(), 0.25)
        self.assertEqual(self.dna_lowcase.gc_content(), 0.25)
        self.assertEqual(self.rna_regular.gc_content(), 0.25)
        self.assertEqual(self.rna_lowcase.gc_content(), 0.25)

    def test_translate_to_rna(self):
        self.assertEqual(self.dna_regular.transcribe().seq_string, "UUUUAAAACCGGUUUU")
        self.assertEqual(self.dna_lowcase.transcribe().seq_string, "UUUUAAAACCGGUUUU")
        self.assertEqual(print(self.dna_empty.transcribe()), None)

    def test_translated_class(self):
        self.assertIsInstance(self.dna_regular.transcribe(), RNA)

    def test_reverse_seq(self):
        self.assertEqual(self.dna_regular.reverse_complement().seq_string, "TTTTAAAACCGGTTTT")
        self.assertEqual(self.dna_lowcase.reverse_complement().seq_string, "TTTTAAAACCGGTTTT")
        self.assertEqual(print(self.dna_empty.reverse_complement()), None)
        self.assertEqual(self.rna_regular.reverse_complement().seq_string, "UUUUAAAACCGGUUUU")
        self.assertEqual(self.rna_lowcase.reverse_complement().seq_string, "UUUUAAAACCGGUUUU")
        self.assertEqual(print(self.rna_empty.reverse_complement()), None)

    def test_eq(self):
        self.assertEqual(self.dna_regular, self.dna_lowcase)
        self.assertEqual(self.rna_regular, self.rna_lowcase)


if __name__ == '__main__':
    unittest.main()
