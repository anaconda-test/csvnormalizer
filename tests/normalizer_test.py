from contextlib import redirect_stdout
from decimal import Decimal
import io
from unittest import mock
from unittest import TestCase

from csvnormalizer import normalizer


SAMPLE_HEADERS = 'TIMESTAMP,ADDRESS,ZIP,FULLNAME,FOODURATION,BARDURATION,TOTALDURATION,NOTES'


class NormalizerTest(TestCase):
    def test_fieldnames(self):
        input_fieldnames = ['Uppercase','CamelCase','snake_case','two words','with	tab','è la verità','かわいい']
        expected = ['UPPERCASE','CAMELCASE','SNAKE_CASE','TWO WORDS','WITH	TAB','È LA VERITÀ','かわいい']
        self.assertEqual(expected, normalizer.fieldnames(input_fieldnames))

    def test_duration(self):
        self.assertEqual(Decimal('3723.04'), normalizer.duration('01:02:03.04'))

    def test_duration_over_24_hours(self):
        # Some parsing utils assume it's a time of day. Handle 24+ hours.
        self.assertEqual(Decimal('180003.04005'),
                         normalizer.duration('50:00:03.040050'))

    def test_total_duration(self):
        row = {
            'FooDuration': '01:02:03.04',
            'BarDuration': '50:00:03.040050',
        }
        self.assertEqual(Decimal('183726.08005'),
                         normalizer.total_duration('>^.^<', row))

    def test_duration_over_24_hours(self):
        # Some parsing utils assume it's a time of day. Handle 24+ hours.
        self.assertEqual(Decimal('180003.04005'),
                         normalizer.duration('50:00:03.040050'))

    def test_timestamp_assume_pacific(self):
        self.assertEqual('2016-02-29T15:11:11-05:00',
                         normalizer.timestamp('2/29/16 12:11:11 PM'))

    def test_timestamp_named_tz(self):
        # Note, test covers cases not in the spec, but `dateutil` is just so
        # handy we get it for free!
        self.assertEqual('2011-04-01T07:00:00-04:00',
                         normalizer.timestamp('4/1/11 11:00:00 AM UTC'))

    def test_timestamp_offset_tz(self):
        # Note, test covers cases not in the spec, but `dateutil` is just so
        # handy we get it for free!
        self.assertEqual('2014-03-12T02:00:00-04:00',
                         normalizer.timestamp('3/12/14 12:00:00 AM -06:00'))

    def test_zip_regular(self):
        self.assertEqual('94121', normalizer.NORMALIZERS['ZIP']('94121'))

    def test_zip_zero_prefix(self):
        self.assertEqual('00001', normalizer.NORMALIZERS['ZIP']('1'))


    def test_zip_zero_prefix(self):
        self.assertEqual('00001', normalizer.NORMALIZERS['ZIP']('1'))


    def test_process_sample(self):
        out = io.StringIO()
        with redirect_stdout(out):
            with open('samples/sample.csv') as f:
                normalizer.process(f)

        out_lines = out.getvalue().splitlines()
        self.assertEqual(10, len(out_lines))
        with open('samples/out_sample.csv') as expected:
            for i, line in enumerate(expected):
                self.assertEqual(out_lines[i], line.strip())
