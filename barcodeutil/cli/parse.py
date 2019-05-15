import zxing
from easycli import Argument, Root, SubCommand

from ..decoder import decode_barcode


class ParseCommand(SubCommand):
    __command__ = 'parse'
    __arguments__ = [
        Argument(
            '-V', '--version',
            action='store_true',
            help='Shows version'
        ),
        Argument(
            '-i', '--image',
            default='',
            help='Give path to the image of driver license barcode.'
        ),
    ]

    def __call__(self, args):
        image = args.image
        reader = zxing.BarCodeReader()
        barcode = reader.decode(image)
        result = decode_barcode(barcode.raw)
        print(result)


class Main(Root):
    __help__ = 'Driving License Barcode Parser'
    __completion__ = True

    __arguments__ = [
        ParseCommand
    ]


if __name__ == '__main__':
    Main().main()
