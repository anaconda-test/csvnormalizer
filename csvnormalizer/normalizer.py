import csv
from decimal import Decimal
import io
import sys

from dateutil.parser import parse as dateparse
from dateutil import tz


EASTERN = tz.gettz("America/New_York")
PACIFIC = tz.gettz("America/Los_Angeles")


def run():
    process(sys.stdin.buffer)


def process(raw_input_buffer):
    wrapper = io.TextIOWrapper(
        raw_input_buffer, encoding='utf-8-sig', errors='replace')
    reader = csv.DictReader(wrapper)
    writer = csv.DictWriter(sys.stdout, fieldnames(reader.fieldnames))
    writer.writeheader()
    for row in reader:
        out_row = {}
        for k, v in row.items():
            norm_fn = NORMALIZERS.get(k, lambda v, r: v)
            try:
                out_row[k.upper()] = norm_fn(v, row)
            except:
                print('WARNING: Dropping invalid row due to malformed'
                      ' value "{v}" for column "{k}".'.format(v=v, k=k),
                      file=sys.stderr)
                out_row = None
                break
        if out_row:
            writer.writerow(out_row)


def fieldnames(field_list):
    return [f.upper() for f in field_list]


def timestamp(raw, row=None):
    dt = dateparse(raw)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=PACIFIC)
    return dt.astimezone(EASTERN).isoformat()


def duration(raw, row=None):
    parts = [Decimal(t) for t in raw.strip().split(':')]
    return parts[0]*60*60 + parts[1]*60 + parts[2]


def total_duration(raw, row):
    return duration(row['FooDuration']) + duration(row['BarDuration'])


NORMALIZERS = {
    'BarDuration': duration,
    'FooDuration': duration,
    'Timestamp': timestamp,
    'TotalDuration': total_duration,
    'ZIP': lambda x, row=None: '{:0>5d}'.format(int(x)),
}
