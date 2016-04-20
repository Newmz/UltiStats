#this function writes the faulty lines to an output file
def report_faulty_lines(successLines, fname):
	with open(fname, "w") as output:
		output.write("Faulty lines for "+fname.split(".")[0])
		for lineNum, line in enumerate(successLines):
			if not line:
				output.write("line "+str(lineNum+2)+"\n")