import eng_to_ipa as ipa

# List of IPA vowel symbols
ipa_vowels = ['i', 'ɪ', 'e', 'ɛ', 'æ',
              'ə', 'ʌ', 'ɜ', 'ɑ', 'ɒ', 
              'ɔ', 'o', 'ʊ', 'u',
              # syllabic 'l', and 'schwa + r'
              'ɚ', 'ɫ']
#ipa_diphthongs = ['aɪ', 'aj', 'aʊ', 'eɪ', 'ej',
#                  'oʊ', 'ɔɪ', 'oj', 'ɪə', 'eə', 'ʊə']

ipa_consonants = ['p', 'b', 't', 'd', 'k', 'g', 
                  'f', 'v', 'θ', 'ð', 's', 'z', 
                  'ʃ', 'ʒ', 'tʃ', 'dʒ', 'h',
                  'm', 'n', 'ŋ',
                  'l', 'r', 'ɹ', 'w', 'j', 'y']

def divide_into_syllables(word):
    # Transcribe word to IPA symbols
    ipa_word = ipa.convert(word)
    
    # Initialize syllable list and current syllable
    syllables = []
    current_syllable = ''
    
    # Flag to indicate if we are at the first syllable
    first_syllable = True
    
    # Iterate over each character in the IPA transcription
    for char in ipa_word:
        if char in ipa_vowels:
            if current_syllable and not first_syllable:
                # Append the current syllable to the list
                syllables.append(current_syllable)
                current_syllable = char
            else:
                current_syllable += char
                first_syllable = False
        elif char in ipa_consonants:
            current_syllable += char
    
    # Add the last syllable if it exists
    if current_syllable:
        syllables.append(current_syllable)
    
    return syllables

# Example usage for multiple words
words = ["example", "machine", "apple", "constitution", "accent", "cup"]
print("Word\tSyllables\tNumber of Syllables")
print ("")
for word in words:
    syllables = divide_into_syllables(word)
    syllable_counter = ipa.syllable_count(word)
    print(f"{word}\t{syllables}\t{syllable_counter}")
