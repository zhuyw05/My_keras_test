a="./keras/keras.json"
def to_theano():
	old=open(a).read()
	new=old.replace("tensorflow","theano")
	open(a,"w").write(new)

def to_tensorflow():
	old=open(a).read()
	new=old.replace("theano","tensorflow")
	open(a,"w").write(new)
	