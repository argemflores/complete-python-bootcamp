# string_splosion

# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    new_str = ''
    
    for i, s in enumerate(str):
        new_str += str[:i+1]
    
    return new_str
