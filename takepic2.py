import os,sys,subprocess

def fname(**kwargs):
	fname = kwargs.get("fname","defaultpic.jpg")
	while True:
		if fname in os.listdir(os.getcwd()):
			iext = fname.index(".")
			for i in range(1, iext):
				if not trail.isdigit():
					break
			trail = (0,"1") if i==1 else (i-1,fname[iext-i:iext])
			fname = fname[:iext - trail[0]] + trail[1] + fname[iext:]
		else:
			break
	return fname

def takepic(fn):
	subprocess.call(["raspistill", "-o", fn])

if __name__ == "__main__":
	arg = dict(fname = sys.argv[1]) if len(sys.argv) > 1 else {}
	fn = tname(**arg)
	takepic(fn)
	print 'done'
	