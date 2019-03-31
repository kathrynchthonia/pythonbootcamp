playlist = {
    'title': 'Oddyssey',
    'author': 'Beatrice Nox',
    'songs': [
        {'title': 'I Am the Walrus', 'artist': [
            'The Beatles'], 'duration': 3.33},
        {'title': 'Strawberry Fields', 'artist': [
            'The Beatles'], 'duration': 3.33},
        {'title': 'Across the Universe', 'artist': [
            'The Beatles'], 'duration': 3.33},
        {'title': 'Let it Be', 'artist': ['The Beatles'], 'duration': 3.33},
        {'title': 'Lucy in the Sky with Diamonds',
         'artist': ['The Beatles'], 'duration': 3.33},
        {'title': 'A Day in the Life', 'artist': [
            'The Beatles'], 'duration': 3.33},
        {'title': 'Yellow Submarine', 'artist': [
            'The Beatles'], 'duration': 3.33}
    ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)
