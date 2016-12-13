## Manual fake generation for use in the DES-GW difference imaging pipeline
### prepmag20.py

The main code here (prepmag20.py) generates a list of coordinates for magnitude 20 fakes with uniform spacing in RA and DEC in a specified area. It also generates a ds9 region file that will put 2 arcsec radius green circles around the location of each of the fakes you want to generate. Since it only needs to be used in specific test situations, the input hasn't really been streamlined. 

At the top of the file, you need to set 4 variables (**topdec**, **botdec**, **bigra**, **lilra**); these are, ideally, the maximum and minimum extents in each direction of your image. When I developed this code as an offshoot of the original, I was testing on one CCD, and that information is in the header of any DES single-CCD image (**RACMIN**, **RACMAX**, **DECCMIN**, **DECCMAX**). Of course, these don't need to be exact. Beneath that, the variables **delra** and **deldec** set the spacing in each direction, in *arcminutes*.

You can then specify the names of the two output files. For the fake coordinate file itself, I recommend you leave it as **mag20.radec** for easier uploading to the database. For the ds9 region file, it doesn't really matter, as you'll just use it manually.

### upload.csh

This code is used to upload your newly generated fake coordinates to the database, from which they will be pulled for use in the diffimg pipeline. At the top, make sure the four variables are set as follows:
```
set table = SNFAKE
set schema      = marcelle
set fakeversion = KBOMAG20NGC1433
set idoffset    = 10000000
```
