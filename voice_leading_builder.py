chord_mapping = {
    "I": [0, 4, 7, 11], 
    "viidim/iii": [3, 6, 9, 12], 
    "V/iii": [11, 15, 18, 21], 
    "viidim/vi": [8, 11, 14, 17], 
    "V/vi": [4, 8, 11, 14], 
    "viidim/ii": [1, 4, 7, 10], 
    "V/ii": [9, 13, 16, 19], 
    "viidim/V": [6, 9, 12, 15], 
    "V/V": [2, 6, 9, 12], 
    "viidim/IV": [4, 7, 10, 13], 
    "V/IV": [0, 4, 7, 10], 
    "iii": [4, 7, 11, 14], 
    "vi": [9, 12, 16, 19], 
    "IV": [5, 9, 12, 16], 
    "ii": [2, 5, 12, 16], 
    "viidim": [11, 14, 17, 22], 
    "V6/4": [7, 12, 16, 19], 
    "N6": [5, 8, 13, 17], 
    "+6": [8, 12, 14, 18], 
    "V": [7, 11, 14, 17],
    "viidim/VII": [9, 12, 15, 18],
    "V/VII": [5, 9, 12, 15],
    "viidim/III": [2, 5, 8, 11],
    "V/III": [10, 14, 17, 20],
    "iv": [5, 8, 12, 15],
    "VII": [10, 14, 17, 20],
    "III": [3, 7, 10, 14],
    "VI": [8, 12, 15, 19],
    "iidim": [2, 5, 8, 11],
    "i": [0, 3, 7, 10]
}

key_to_num = {
    'C': 0, 'C#': 1, 'Db': 1,
    'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6,
    'Gb': 6, 'G': 7, 'G#': 8,
    'Ab': 8, 'A': 9, 'A#': 10,
    'Bb': 10, 'B': 11
}

def get_chord_notes(key: str, roman_numeral: str) -> list:
    chord = chord_mapping[roman_numeral]
    offset = key_to_num[key]
    return [note + offset for note in chord]

def octave_transform(input_chord, root):
    # Squish notes into a single octave and sort from lowest to highest
    return sorted([(root + (x % 12)) for x in input_chord])

def t_matrix(chord_a, chord_b):
    # Get the distances between the notes of two chords
    root = chord_a[0]
    chord_a_transformed = octave_transform(chord_a, root)
    chord_b_transformed = octave_transform(chord_b, root)
    return [b - a for a, b in zip(chord_a_transformed, chord_b_transformed)]

def voice_lead(chord_a, chord_b):
    # Voice lead from chord_a to chord_b
    root = chord_a[0]

    # Calculate the mapping of notes in chord_a to the sorted version
    a_leadings = [(x, octave_transform(chord_a, root).index(root + (x % 12))) for x in chord_a]
    
    # Calculate the t_matrix
    t_matrix_ab = t_matrix(chord_a, chord_b)
    
    # Calculate the new voicing for chord_b
    b_voicing = [x + t_matrix_ab[y] for (x, y) in a_leadings]
    
    return b_voicing

# # Example chord progression
# chord_progression = [
#     [64, 67, 71],  # Chord E5 Minor
#     [60, 64, 67],  # Chord C5 Major
#     [66, 69, 71],  # Chord Fs5 Minor
#     [71, 74, 79]   # Chord B5 Minor
# ]

# from time import sleep

# # Initialize the last chord to None
# last_c = None

# for a, b in zip(chord_progression, chord_progression[1:]):
#     if last_c is None:
#         # Play the first chord
#         print("Playing:", a)
#         last_c = a
#         sleep(1)
    
#     # Perform voice leading to transition from a to b
#     last_c = voice_lead(last_c, b)
    
#     print("Playing:", last_c)
#     sleep(1)

# TODO
def get_voice_leading(progression_as_str: list, key: str) -> list:
    print(f'''\nFull progression: {progression_as_str}''')

    progression_as_matrix = []
    for chord in progression_as_str:
        progression_as_matrix.append(get_chord_notes(key, chord))
    print(f'''\nProgression matrix: {progression_as_matrix}''')

    return []