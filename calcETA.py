def calcETA (dict)
	oETA = 0
	for key in dict
		route = dict [key]
			for path in route
				oETA += path.ETA
	return oETA 
					

