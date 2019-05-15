from barcodeutil.decoder import decode_barcode


class TestDecodeBarcode:
    def setup_class(cls):
        cls.barcode = '@\n\x1e\rANSI 636025080002DL00410268ZP03090030DLDAQ' \
                        '99999999\nDCSSAMPLE\nDDEU\nDACJANICE\nDDFU\nDADANN\n' \
                        'DDGU\nDCAC\nDCBNONE\nDCDNONE\nDBD10052015\nDBB08041' \
                        '969\nDBA08042023\nDBC2\nDAU066 IN\nDAYBRO\nDAG123 ' \
                        'MAIN STREET\nDAIHARRISBURG\nDAJPA\nDAK171010000  ' \
                        '\nDCF1234567890123456789012345\nDCGUSA\nDCK12345678' \
                        '90123456\nDDB10012015\nDDK1\nDDL1\n\rZPZPAN\nZPB00' \
                        '\nZPC123\n\rZPDNONE\n\r'

        cls.license_result = '\nFirst Name: JANICE\nMiddle Name: ANN\n' \
                               'Mailing Street Address1: 123 MAIN STREET\n' \
                               'Mailing City: HARRISBURG\nMailing Jurisdiction' \
                               ' Code: PA\nMailing Postal Code: 171010000  \n' \
                               'Height in FT_IN: 066 IN\nEye Color: BRO\n' \
                               'License Expiration Date: 08042023\nDate of' \
                               ' Birth: 08041969\nSex: Female\nLicense or ID ' \
                               'Document Issue Date: 10052015\nJurisdiction-' \
                               'specific vehicle class: C\nJurisdiction-' \
                               'specific restriction codes: NONE\nJurisdiction' \
                               '-specific endorsement codes: NONE\nDocument ' \
                               'Discriminator: 1234567890123456789012345\n' \
                               'Country territory of issuance: USA\nInventory' \
                               ' Control Number: 1234567890123456\nLast Name:' \
                               ' SAMPLE\nCard Revision Date: 10012015\nFamily' \
                               ' Name Truncation: U\nFirst Names Truncation: U\n' \
                               'Middle Names Truncation: U\nOrgan Donor ' \
                               'Indicator: Yes\nVeteran Indicator: 1'

    def test_decode(self):
        print(decode_barcode(self.barcode))
        print(self.license_result)
        assert decode_barcode(self.barcode) == self.license_result


if __name__ == '__main__':
    pass
