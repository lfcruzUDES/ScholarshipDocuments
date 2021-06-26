import argparse

from shipdoc.scholarship_docs import ScholarshipDocs


def main():
    """ Execute de commands. """

    parser = argparse.ArgumentParser(
        description='Merge students documents.',
        prog='shipdocs',
    )

    parser.add_argument(
        'exec',
        help='Execute process.',
    )

    parser.add_argument(
        '-id',
        '--ssid',
        action='store',
        help='Select spreadsheet id.'
    )

    parser.add_argument(
        '-nr',
        '--name_range',
        action='store',
        help='Set a name range.'
    )

    args = parser.parse_args()

    ss_id = args.ssid if args.ssid else None
    name_range = args.name_range if args.name_range else None

    ship = ScholarshipDocs(
        ss_id=ss_id,
        range_name=name_range,
    )
    ship.process()
