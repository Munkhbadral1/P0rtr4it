with open('output.txt', 'w') as file:
    for first_letter in range(ord('A'), ord('Z')+1):
        for second_letter in range(ord('A'), ord('Z')+1):
            for number in range(0, 100):
                code = f'{chr(first_letter)}.{chr(second_letter)}{number:02d}'
                url = f'https://lms.must.edu.mn/Image?code={code}'
                file.write(url + '\n')
                print(f"Wrote URL for {code}")
