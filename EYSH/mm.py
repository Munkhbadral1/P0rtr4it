with open('output.txt', 'w') as file:
    for i in range(213000000, 213001447):
        url = f'https://eyesh.eec.mn/uploads/pupilslastyear/{i}.jpg'
        file.write(url + '\n')
        print(f"Wrote URL for {i}.jpg")
