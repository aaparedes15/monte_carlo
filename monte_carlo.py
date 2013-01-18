def monte_carlo(x,xerr,function,times=1000):
	'''
	input:
		x: array of lenth n
		xerr: array for the value for uncertanty of x of lenth n
		function: the error that the monte carlo simulation will be based on this function
			NOTE: The function has to one in which there is only one input array
		for now, just adjust the program for the function you want.
		time: the amount of test samples the simulation will use

	output:
		sigma: the monte carlo simulation standard deviation

	usage:
		from monte_carlo import monte_carlo as mc
		mc(x,xerr,function,times=10000)

	Example:
		import numpy as np
		from monte_carlo import monte_carlo as mc
		
		x = np.array([4,5,6])
		xerr = np.array([.2,.3,.4])

		function = np.std
		
		mc(x,xerr,function)
			out --> .4

	Author: Anthony Albert Paredes
	Version: 1.0
	August 4, 2011
	'''

	# import needed modules
	import numpy as np

	# an array for later
	function_output = np.array([])	
	
	for j in xrange(times):
	
		# create arrays of gaussian-normal values with a std of the input errors.
		x_new = np.array([])

		for i in xrange(len(x)):
			x_new = np.append(x_new, x[i] + (np.random.randn() * xerr[i]))

		function_output = np.append(function_output, function(x_new))

	sigma = np.std(function_output)

	return sigma






















