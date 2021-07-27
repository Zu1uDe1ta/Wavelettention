#----------------------------------------------------------------#
#																 #
#																 #
#																 #
#																 #
#----------------------------------------------------------------#


def main(): 
	cntr = 1

	for h in range (0, 4): 

		for m in range (0, 6):

			for s in range (0, 10): 

				print(cntr, "). [", h, ":", m, ":", s, "]")
				cntr = cntr + 1

	print("\nTime has ended.")


main()