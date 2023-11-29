# Skriv ett program som översätter ett svenskt datum till amerikanskt form.

# Datum i USA dd/mm/åå
# Datum i Sverige åååå-mm-dd

x = input('Skriv ett Svenk datum, åååå-mm-dd: ')

år = x [2:4]
mån = x [5:7]
dag = x [8:]

n = mån + '/' + dag + '/' + år
print ('Det Amerikanska datumet är: ' + n)