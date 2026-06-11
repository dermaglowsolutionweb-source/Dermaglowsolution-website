import urllib.request

req = urllib.request.Request(
    'https://upload.wikimedia.org/wikipedia/commons/8/82/India_States_Blank.svg',
    headers={'User-Agent': 'Mozilla/5.0'}
)

try:
    with urllib.request.urlopen(req) as response:
        with open('images/india-map-detailed.svg', 'wb') as out_file:
            out_file.write(response.read())
    print("Download successful")
except Exception as e:
    print(f"Error: {e}")
