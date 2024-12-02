# Function 
def matchingShoes(n):
    
    leftShoes = {}
    rightShoes = {}
    
    for i in range (n):
        randLett = input('Masukkan kata acak => ')
        result = ''.join([char for char in randLett if not char.islower()])
        size = ''.join([char for char in result if char.isdigit()])
        side = ''.join([char for char in result if char.isupper()])
        
        if side == 'L':
            if size in leftShoes:
                leftShoes[size] += 1
            else:
                leftShoes[size] = 1
        elif side == 'R':
            if size in rightShoes:
                rightShoes[size] += 1
            else:
                rightShoes[size] = 1
                
    pairs = 0
    for size in leftShoes:
        if size in rightShoes:
            pairs += min(leftShoes[size], rightShoes[size])
    return pairs

# Input
n = int(input('Masukkan jumlah baris => '))

# Output
pairResult = matchingShoes(n)
print(pairResult) 
