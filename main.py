from barcode import Code128
from barcode.writer import ImageWriter

def Barcoding(clientid, abonid):
    with open(f'somefile{abonid}.jpeg', 'wb') as f:
        Code128(str(clientid) + '-' + str(abonid), writer=ImageWriter()).write(f)

if __name__ == "__main__":
    Barcoding(int(input()), int(input()))