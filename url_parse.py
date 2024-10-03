from urllib.parse import urlparse

# The URL you have
url = "http://10.235.11.27/start_b.htm"

# Parse the URL to extract the IP address
parsed_url = urlparse(url)
ip_address = parsed_url.hostname

# Split the IP address into a list of octets
octets = ip_address.split('.')

# Extract the last octet (the 4th one)
last_octet = octets[3]

# Print or use the last octet as needed
print(f"The last octet of the IP address is: {last_octet}")









#another code
url = "http://10.235.11.27/start_b.htm"

# Split the URL to isolate the IP part
ip = url.split('/')[2]  # Get '10.235.11.27'

# Split the IP to get individual octets
octets = ip.split('.')   # ['10', '235', '11', '27']

# Get the fourth octet
fourth_octet = octets[3]  # '27'

print(fourth_octet)

