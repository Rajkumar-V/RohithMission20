Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/mupputur/Desktop/RohitMission20/FileOperations/example2.py =
India (Hindi: Bharat), officially the Republic of India (Hindi: Bharat Ga?arajya),[20] is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[e] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia.
>>> 
>>> 
>>> str1 = "Indian Ocean on the south"
>>> str1
'Indian Ocean on the south'
>>> words = str1.split()
>>> words
['Indian', 'Ocean', 'on', 'the', 'south']
>>> 
>>> for word in words:
	print(word)

	
Indian
Ocean
on
the
south
>>> for word in words:
	if word[0] == 's':
		print(word)

		
south
>>> 
>>> 
