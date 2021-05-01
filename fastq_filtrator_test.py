import unittest
import subprocess

process = subprocess.Popen(['python', 'fastq_filtrator.py', '--output_base_name', 'test', 'fa.fastq'])
process.communicate()

with open('test.fastq', 'r') as fh:
    simple_run = []
    for line in fh:
        simple_run.append(line.rstrip())

de_process = subprocess.Popen(['rm', 'test.fastq'])
de_process.communicate()

process = subprocess.Popen(['python', 'fastq_filtrator.py',
                            '--min_length', '6', '--output_base_name', 'test', 'fa.fastq'])
process.communicate()

with open('test.fastq', 'r') as fh:
    short_run = []
    for line in fh:
        short_run.append(line.rstrip())

de_process = subprocess.Popen(['rm', 'test.fastq'])
de_process.communicate()

process = subprocess.Popen(['python', 'fastq_filtrator.py',
                            '--gc_bounds', '50', '--output_base_name', 'test', 'fa.fastq'])
process.communicate()

with open('test.fastq', 'r') as fh:
    gc_run = []
    for line in fh:
        gc_run.append(line.rstrip())

de_process = subprocess.Popen(['rm', 'test.fastq'])
de_process.communicate()


class FilterTest(unittest.TestCase):
    pass

    def test_simple_run(self):
        self.assertEqual(simple_run[0], 'fu1')
        self.assertEqual(simple_run[4], 'fu2')
        self.assertEqual(simple_run[8], 'fi3')
        self.assertEqual(simple_run[12], 'fu4')
        self.assertTrue(len(simple_run) == 16)

    def test_short_run(self):
        self.assertEqual(short_run[0], 'fu1')
        self.assertEqual(short_run[4], 'fi3')
        self.assertEqual(short_run[8], 'fu4')
        self.assertTrue(len(short_run) == 12)

    def test_gc_run(self):
        self.assertEqual(gc_run[0], 'fi3')
        self.assertTrue(len(gc_run) == 4)


if __name__ == '__main__':
    unittest.main()
