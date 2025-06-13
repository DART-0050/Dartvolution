import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'abc')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d') # matches any digit
# pattern = re.compile(r'\bHa') # matches any word boundary
# pattern = re.compile(r'\BHa') # matches any Ha which is not word boundary
# pattern = re.compile(r'^Start') # matches any word which starts with Start
# pattern = re.compile(r'end$') # matches any word which ends with end
# pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') # Takes - or . in middle
# pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
# pattern = re.compile(r'[^a-zA-Z]')  # matches any non-alphabet character

# pattern = re.compile(r'Mr\.?') # matches Mr or Mr.
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
 
# pattern = re.compile(r'[a-zA-Z.-0-9]+@[a-zA-Z0-9-]+\.(com|edu|net)')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# MATCHING WITH FINDITER (NORMAL AND GROUPS)

    # matches = pattern.finditer(urls)

    # for match in matches:
    #     print(match.group(2))



# READING FROM A FILE

    # with open('data.txt', 'r') as f:
    #     contents = f.read()

    #     matches = pattern.finditer(contents)
        
    #     for match in matches:
    #         print(match)