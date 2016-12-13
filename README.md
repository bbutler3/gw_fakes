## Manual fake generation for use in the DES-GW difference imaging pipeline
### `prepmag20.py`

The main code here (prepmag20.py) generates a list of coordinates for magnitude 20 fakes with uniform spacing in RA and DEC in a specified area. It also generates a ds9 region file that will put 2 arcsec radius green circles around the location of each of the fakes you want to generate. Since it only needs to be used in specific test situations, the input hasn't really been streamlined. 

At the top of the file, you need to set 4 variables (`topdec`, `botdec`, `bigra`, `lilra`); these are, ideally, the maximum and minimum extents in each direction of your image. When I developed this code as an offshoot of the original, I was testing on one CCD, and that information is in the header of any DES single-CCD image (`RACMIN`, `RACMAX`, `DECCMIN`, `DECCMAX`). Of course, these don't need to be exact. Beneath that, the variables `delra` and `deldec` set the spacing in each direction, in *arcminutes*.

You can then specify the names of the two output files. For the fake coordinate file itself, I recommend you leave it as **mag20.radec** for easier uploading to the database. For the ds9 region file, it doesn't really matter, as you'll just use it manually.

### `upload.csh`

This code is used to upload your newly generated fake coordinates to the database, from which they will be pulled for use in the diffimg pipeline. At the top, make sure the four variables are set as follows, _with the exception of_ `fakeversion`:
```Shell
set table = SNFAKE
set schema      = marcelle
set fakeversion = KBOMAG20NGC1433
set idoffset    = 10000000
```
You should change `fakeversion` to something new for each new _area_ of fakes you generate (if you're just trying the same CCD again with different fake spacing, for example, maybe leave the name the same so the database table doesn't get insanely large over time). The convention I was using when I last edited this file was just to tack on the name of the particular bright galaxy I was using to the end of `KBOMAG20`. Whatever convention you use will become important in the next step.

### Editing the `MAKESCRIPT_DIFFIMG_TEMPLATE.INPUT` file before running through the pipeline

Before you run the `DAGMAKER.sh` script, you'll need to edit the `MAKESCRIPT_DIFFIMG_TEMPLATE.INPUT` file to match the `fakeversion` you specified in the `upload.csh` file. This should be on line 61 (if it ends up not being exactly at that location, it's the first line starting with `DOFAKE_OPTIONS:`. At the very end of the line, you need to specify `-dbVersion_SNFake`; this is where you put your `fakeversion` name.

After all this, assuming you have the rest of the requisites for running the pipeline in order, you can run the dagmaker and submit the dag. 
