import glob, os

def rename(dir, pattern, titlePattern):
	for pathAndFilename in glob.iglob(os.path.join(dir,pattern)):
		print pathAndFilename
		base = os.path.basename(pathAndFilename)
		print base
		splitPAF = base.split('exr.',1)
		print splitPAF
		title =  ''.join(splitPAF)
		print title
		ext = '.exr'
		#title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		os.rename(pathAndFilename,os.path.join(dir,titlePattern % title + ext))
		

		
rename(r'C:\Users\cb3082\Documents\FILM_RENDERS\images',r'*.exr.*',r'%s')