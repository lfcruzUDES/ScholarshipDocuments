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
        '-m',
        '--mode_magick',
        help=('By default program usages PyPDF4 to merge documents, if you'
              ' select this mode program usages Imagemagick.'),
        action='store_true',
    )

    args = parser.parse_args()

    ship = ScholarshipDocs()

    if args.mode_magick:
        ship.process(mode='magick')
    else:
        ship.process()
