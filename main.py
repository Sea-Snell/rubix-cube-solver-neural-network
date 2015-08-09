from numpy import *
import os









def gradientCheck(theta, network, x, y, lambdaVal):
	e = 0.0001

	tempTheta = theta[0].reshape(theta[0].size, 1)
	for i in range(1, len(theta)):
		tempTheta = vstack((tempTheta, theta[i].reshape(theta[i].size, 1)))

	new = []
	temp = zeros((tempTheta.size, 1), dtype = float64)
	for i in range(tempTheta.size):
		temp[i] = e

		dif1 = tempTheta - temp
		dif2 = tempTheta + temp

		new1 = [dif1[:theta[0].size, :].reshape(network[1], network[0] + 1), dif1[theta[0].size:theta[0].size + theta[1].size, :].reshape(network[2], network[1] + 1), dif1[theta[0].size + theta[1].size:, :].reshape(network[3], network[2] + 1)]
		new2 = [dif2[:theta[0].size, :].reshape(network[1], network[0] + 1), dif2[theta[0].size:theta[0].size + theta[1].size, :].reshape(network[2], network[1] + 1), dif2[theta[0].size + theta[1].size:, :].reshape(network[3], network[2] + 1)]
		
		dif1 = computeGradient(new1, network, x, y, lambdaVal)[0]
		dif2 = computeGradient(new2, network, x, y, lambdaVal)[0]

		new.append((dif2 - dif1) / (2 * e))
		temp[i] = 0
	
	otherDerivitive = computeGradient(theta, network, x, y, lambdaVal)[1]
	newDeriv = otherDerivitive[0].reshape(otherDerivitive[0].size, 1)
	for i in range(1, len(otherDerivitive)):
		newDeriv = vstack((newDeriv, otherDerivitive[i].reshape(otherDerivitive[i].size, 1)))

	for i in range(len(new)):
		print new[i], float(newDeriv[i])








def computeGradient(theta, network, x, y, lambdaVal):
	m = x.shape[0]
	J = 0.0
	gradient = []
	a = []
	z = []
	d = []
	delta = []

	a.append(x)
	a[0] = transpose(a[0])
	a[0] = vstack((ones((1, a[0].shape[1]), dtype = float64), a[0]))
	for i in range(1, len(network)):
		z.append(dot(theta[i - 1], a[i - 1]))
		a.append(sigmoid(z[i - 1]))
		a[i] = vstack((ones((1, a[i].shape[1]), dtype = float64), a[i]))
	a[-1] = a[-1][1:, :]

	y = y.reshape(y.size, 1)
	y = array(array([arange(1, network[-1] + 1)] * m, dtype = int32) == y, dtype = int32)
	y = transpose(y)

	total = 0
	for i in range(len(theta)):
		total += sum(theta[i] ** 2)

	J = (float(1.0 / float(m)) * sum((-y * log(a[-1])) - ((1.0 - y) * log(1.0 - a[-1])))) + ((lambdaVal / (2.0 * m)) * total)


	d.append(a[-1] - y)
	for i in range(1, len(network) - 1):
		z[-1 - i] = vstack((ones((1, z[- 1 - i].shape[1]), dtype = float64), z[- 1 - i]))
		d.append((dot(transpose(theta[-i]), (d[i - 1]))) * sigmoidGradient(z[- 1 - i]))
		d[i] = d[i][1:, :]


	for i in range(1, len(network)):
		delta.append(dot(d[-i], transpose(a[i - 1])))


	for i in range(1, len(network)):
		gradient.append((delta[i - 1] * (1 / float(m))) + ((lambdaVal / float(m)) * hstack((zeros((theta[i - 1].shape[0], 1), dtype = float64), theta[i - 1][:, 1:]))))
	return (J, gradient)


def sigmoid(z):
	return 1.0 / (1.0 + exp(-z))

def sigmoidGradient(z):
	return sigmoid(z) * (1.0 - sigmoid(z))

def randomizeTheta(a, b):
	return (random.uniform(0.0, 1.0, (a, b)) * 2 * 0.12 - 0.12)

def parseInput(fileName):
	size = os.path.getsize(fileName)
	openFile = open(fileName, "r")
	text = openFile.read(size)
	a = text.split("\n")
	ans = []
	for i in range(len(a)):
		if a[i] != "":
			ans.append(map(float, a[i].split()))
			ans[-1] = array(ans[-1], dtype = float64)
	return array(ans)

def saveData(fileName, data):
	openFile = open(fileName, "w+")
	openFile.truncate()
	for i in range(data.shape[0]):
		openFile.write(" ".join(map(str, data[i])))
		openFile.write("\n")

def saveDataList(fileName, data):
	openFile = open(fileName, "w+")
	openFile.truncate()
	openFile.write(" ".join(map(str, data)))
	openFile.write("\n")

def gradientDescent(theta, network, x, y, lambdaVal, learningRate, iterations):
	for z in range(1, iterations + 1):
		ans = computeGradient(theta, network, x, y, lambdaVal)
		for i in range(len(ans[1])):
			theta[i] -= learningRate * ans[1][i]
		print "iteration %d | cost %f" % (z, ans[0])
	return theta

def predictOne(x, theta, network):
	a = x
	a = hstack((array([1]), a))
	for i in range(1, len(network)):
		z = (dot(a, transpose(theta[i - 1])))
		a = (sigmoid(z))
		a = hstack((array([1]), a))
	a = a[1:]
	return a.argmax() + 1

def predictSeveral(x, theta, network):
	a = x
	a = hstack((ones((a.shape[0], 1), dtype = float64), a))
	for i in range(1, len(network)):
		z = (dot(a, transpose(theta[i - 1])))
		a = sigmoid(z)
		a = hstack((ones((a.shape[0], 1), dtype = float64), a))
	a = a[:, 1:]
	return a.argmax(axis = 1) + 1

def getRate(x, y, theta, network):
	a = array(predictSeveral(x, theta, network) == y, dtype = int32)
	return float(float(a.sum()) / float(a.shape[0])) * 100.0



print "loading data..."

oldNetwork = parseInput('oldNet.txt')
oldNetwork = oldNetwork[0]
oldNetwork = list(oldNetwork)

data = parseInput('trainData.txt')
x = data[:, :-1]
y = data[:, -1]

network = [72, 1, 7]

if list(oldNetwork) == list(network):
	theta = []
	for i in range(1, len(network)):
		theta.append(parseInput('theta' + str(i) + '.txt'))

print "data loaded."

if list(oldNetwork) != list(network):
	print "generating theta..."
	theta = []
	for i in range(len(network) - 1):
		theta.append(randomizeTheta(network[i + 1], network[i] + 1))
	saveDataList("oldNet.txt", network)

	print "theta generated."



print "training network..."

val = gradientDescent(theta, network, x, y, 1.0, 0.25, 500)

print "training complete."

print "saving theta..."

for i in range(len(val)):
	saveData("theta" + str(i + 1) + ".txt", val[i])

print "theta saved."
print "\n"

print "training gradient: " + str(computeGradient(val, network, x, y, 0.0)[0])
print "training accuracy: " + str(getRate(x, y, val, network))
print "\n"

data = parseInput('validateData.txt')
x = data[:, :-1]
y = data[:, -1]

print "validation gradient: " + str(computeGradient(val, network, x, y, 0.0)[0])
print "validation accuracy: " + str(getRate(x, y, val, network))
print "\n"

data = parseInput('testData.txt')
x = data[:, :-1]
y = data[:, -1]

print "test gradient: " + str(computeGradient(val, network, x, y, 0.0)[0])
print "test accuracy: " + str(getRate(x, y, val, network))
print "\n"

print "all done"

