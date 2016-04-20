from debugging_image import debuggingImage

testData1 = []
for i in range(0,50):
	testData1.append(True)
for i in range(0,50):
	testData1.append(False)

debuggingImage(testData1, "test.csv")