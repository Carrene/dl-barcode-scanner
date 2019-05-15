from barcodeutil.license_fields import driver_license_fields


def decode_barcode(data: str):
    sub_data = data
    splitted = sub_data.split('\n')
    fields = driver_license_fields

    for datum in splitted:

        for field in fields:
            abb = field.get('abbreviation')

            if datum.find(abb) == 0:
                field['in_license'] = True
                field['value'] = datum[len(abb):]

# gender, address, organ donor(ddk, dbh), anything INDICATOR, weight, height
# Mentioned values must be modified

    for field in fields:
        if field.get('abbreviation') == ('DAG' or 'DAH' or 'DAL' or 'DAM'):
            pass

        if field.get('abbreviation') == 'DBC':
            field['value'] = 'Female' if field.get('value') == '2' else 'Male'

        if field.get('abbreviation') == ('DDK' or 'DBH'):
            field['value'] = 'Yes' if field.get('value') == ('1' or 'Y') else 'No'

    license_result = ''

    for field in fields:
        if field.get('in_license'):
            license_result \
                = license_result \
                  + ('\n%s: %s' % (field.get('description'), field.get('value')))

    return license_result
