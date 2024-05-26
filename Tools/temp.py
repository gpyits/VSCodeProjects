import time

letter = 'Z'
letters = ''
letters += '\033[31mZ\033[0m'
letters += f'\033[31m{letter}\033[0m'

print('\033[31mZ\033[0m')
print(f'\033[31m{letter}\033[0m')
print(letters, flush=True)

# Split the letters string into formatted segments.
segments = ['\033[31mZ\033[0m', f'\033[31m{letter}\033[0m']

for segment in segments:
    time.sleep(0.5)
    print(segment, end=' ', flush=True)