matrix_init = ['0'] * 21
matrix = [matrix_init]

for _ in range(19):
    adding = ['0']
    adding.extend(list(input().split()))
    adding.append('0')
    matrix.append(adding)

matrix.append(matrix_init)

#print(matrix)

#가로
def concave_descriminator(matrix):
    descriminator_1 = [('0111110'), ('0111112'), ('2111110'), ('2111112')]
    descriminator_2 = [('0222220'), ('0222221'), ('1222220'), ('1222221')]

    for col in range(1,20):
        for desc in descriminator_1:
            col_a = ''.join(matrix[col])
            if desc in col_a:    
                indexed = col_a.index(desc)
                print(1)
                print(col, indexed + 1)
                return

    for col in range(1,20):
        for desc in descriminator_2:
            col_b = ''.join(matrix[col])
            
            #print(col_a)
            if desc in col_b:    
                indexed = col_b.index(desc)
                print(2)
                print(col, indexed + 1)
                return


    #세로
    transed_mat =list(map(list, zip(*matrix)))

    #print(transed_mat)


    for col in range(1,20):
        for desc in descriminator_1:
            col_a = ''.join(transed_mat[col])
            if desc in col_a:    
                indexed = col_a.index(desc)
                print(1)
                print(indexed + 1, col)
                return

    for col in range(1,20):
        for desc in descriminator_2:
            col_b = ''.join(transed_mat[col])
            #print(col_b)

            if desc in col_b:    
                indexed = col_b.index(desc)
                print(2)
                print(indexed + 1, col)
                return

    # 대각선 (n,n)
    for distortion in range(21):
        line_a = []
        line_b = []
        for col in range(21 - distortion):
            line_a.append(matrix[col][col+distortion])
            line_b.append(matrix[col+distortion][col])

        str_a = ''.join(line_a)
        str_b = ''.join(line_b)
        
        line_a.clear()
        line_b.clear()

        for desc in descriminator_1:
            if desc in str_a:    
                indexed = str_a.index(desc)
                print(1)
                print(indexed+1, indexed + 1 + distortion)
                return
            
        for desc in descriminator_1:
            if desc in str_b:    
                indexed = str_b.index(desc)
                print(1)
                print(indexed+1 + distortion, indexed + 1)
                return

        for desc in descriminator_2:
            if desc in str_a:    
                indexed = str_a.index(desc)
                print(2)
                print(indexed+1, indexed + 1 + distortion)
                return
        for desc in descriminator_2:
            if desc in str_b:    
                indexed = str_b.index(desc)
                print(2)
                print(indexed+1 + distortion, indexed + 1)
                return    
    
    # 대각선 (n,19-n)

    for distortion in range(21):
        line_a = []
        line_b = []
        for col in range(21 - distortion):
            line_a.append(matrix[col + distortion][20 - col])
            line_b.append(matrix[col][20 - col - distortion])

        str_a = ''.join(line_a)
        str_b = ''.join(line_b)
        
        line_a.clear()
        line_b.clear()

        #print(str_a)
        #print(str_b)
        for desc in descriminator_1:
            if desc in str_a:    
                indexed = str_a.index(desc)
                print(1)
                print(indexed + 5 + distortion, -indexed + 15)
                return
            
        for desc in descriminator_1:
            if desc in str_b:    
                indexed = str_b.index(desc)
                print(1)
                print(indexed + 5, -indexed + 15 - distortion)
                return
            
        for desc in descriminator_2:
            if desc in str_a:    
                indexed = str_a.index(desc)
                print(2)
                print(indexed + 5 + distortion, -indexed + 15)
                return
            
        for desc in descriminator_2:
            if desc in str_b:    
                indexed = str_b.index(desc)
                print(2)
                print(indexed + 5, -indexed + 15 - distortion)
                return
            
    print(0)
    return




concave_descriminator(matrix)
