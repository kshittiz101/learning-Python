random = "Nepal,      India, China, USA, UK"
list_of_country = random.split(',')
print(list_of_country)

# remove extras spaces 
text = "apple,       banana, cherry"
result = [item.strip() for item in text.split(",")]
print(result)


# bytearray
# In Python, a byte array (bytearray) is a mutable sequence of bytes — meaning it stores binary data (numbers between 0–255) that you can change after creation.
# It’s often used when working with binary files, network data, encryption, or image/audio processing.

