from glob import glob
import easyaccess as ea
import numpy as np
import os

connection = ea.connect()

cursor = connection.cursor()

query = "select i.filename,path from image i,file_archive_info f where i.filename=f.filename and racmin < 55.506 and racmax > 55.506 and deccmin < -47.221 and deccmax > -47.221 and i.filetype='red_immask'"

QQ=cursor.execute(query)

QQ.description

header = [item[0] for item in cursor.description]
rows = cursor.fetchall()  ## Bring the data
cols = np.array(zip(*rows))

for col in range(len(cols[0])):
	band = cols[0][col].split('_')[1]
	if band=='i' or band=='z':
		root = "https://desar2.cosmology.illinois.edu/DESFiles/desarchive/"
		path = cols[1][col]
		filename = cols[0][col]
		fullname = root + path + "/" + filename + ".fz"
		print fullname
		wgetme = 'wget  --user rbutler --password rbu70chips --no-check-certificate -nv '
		outdir = ' -P ./NGC1433'
		command = wgetme + fullname + outdir
		os.system(command)


