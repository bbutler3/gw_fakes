import numpy as np

# maximum and minimum extents of the area you want
topdec = -47.109
botdec = -47.262
bigra = 55.715
lilra = 55.273

# set spacing of Mag20 fakes in RA,DEC directions in arcminutes
delra = 1
deldec = 1

# prep output file
outfile = 'mag20.radec'
ds9outfile = 'mag20ds9.reg'

file = open(outfile, 'w+')
ds9file = open(ds9outfile, 'w+')

# adjustment to ensure full coverage
topdec = topdec + 2.*(1./60.)*deldec
botdec = botdec - 1.*(1./60.)*deldec
bigra = bigra + 2.*(1./60.)*delra
lilra = lilra - 2.*(1./60.)*delra

# only relevant if you actually go over RA=0.00
# avoid RA=0.00000 by this many arcminutes
zeroshift = 2    # should be smaller than delra
#zeroshift = float(zeroshift)

maxi = (1.-deldec/60.)*2.*60./deldec
i = 0
dec = topdec
ra = bigra
while (dec<=topdec and dec>=botdec):
	dec = (topdec-(deldec/60.))-i*(deldec/60.)
	strdec = '{0:+6f}'.format(dec)
	maxj = (bigra-delra)*(60./delra)*np.cos(dec*np.pi/180.)
	j = 0
	#print dec
	ra = lilra
	while (ra<=bigra and ra>=lilra):
		ra = lilra + j*(delra/60.)/np.cos(dec*np.pi/180.)#+(zeroshift/60.)
		strra = '{0:6f}'.format(ra)
		file.write(strra),file.write(' '),file.write(strdec),file.write("\n")	
		ds9file.write('circle '),ds9file.write(strra),ds9file.write('d ')
		ds9file.write(strdec),ds9file.write('d '),ds9file.write('2"\n')
		j = j+1
	i = i+1

file.close()
ds9file.close()
