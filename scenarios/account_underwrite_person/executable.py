import balanced

balanced.configure('ak-test-1p1Tsac7gHeMQowL2seB7ieliuAJAufyq')

merchant_data = {
    "phone_number": "+14089999999", 
    "name": "Timmy Q. CopyPasta", 
    "dob": "1989-12", 
    "postal_code": "94110", 
    "type": "person", 
    "street_address": "121 Skriptkid Row"
}

account = balanced.Account().save()

try:
    account.add_merchant(merchant_data)
except balanced.exc.MoreInformationRequiredError as ex:
    # could not identify this account.
    print 'redirect merchant to:', ex.redirect_uri
except balanced.exc.HTTPError as error:
    # TODO: handle 400 and 409 exceptions as required
    raise