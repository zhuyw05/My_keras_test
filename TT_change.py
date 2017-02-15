import sys
a=r"/home/ubuntu/.keras/keras.json"
def to_theano():
	old=open(a).read()
	new=old.replace("tensorflow","theano")
	open(a,"w").write(new)

def to_tensorflow():
	old=open(a).read()
	new=old.replace("theano","tensorflow")
	open(a,"w").write(new)

if __name__ == '__main__':
	print(sys.argv)
	print(sys.argv[1])
	if sys.argv[1]=="tensorflow":
		to_tensorflow()
	elif sys.argv[1]=="theano":
		to_theano()
	else:
		print ("Unknown command, try python TT_change.py tensorflow   or python TT_change.py theano")