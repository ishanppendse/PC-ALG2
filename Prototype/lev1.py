def levens(a, b):
    if len(a) < len(b):
        a, b = b, a
    # We will have the length of the smaller string as the number of cols, this makes space complexity as min(len(a),
    # len(b))
    lena = len(a)
    lenb = len(b)
    even = list(range(0, lenb + 1))
    odd = list(range(0, lenb + 1))
    temp = 1
    while temp <= lena:
        count = 0
        if temp % 2:
            while count <= lenb:
                if count == 0:
                    odd[0] = temp
                else:
                    val = (a[temp - 1] != b[count - 1])
                    odd[count] = min(odd[count - 1] + 1, even[count] + 1, even[count - 1] + val)
                count += 1
        else:
            while count <= lenb:
                if count == 0:
                    even[0] = temp
                else:
                    val = (a[temp - 1] != b[count - 1])
                    even[count] = min(even[count - 1] + 1, odd[count] + 1, odd[count - 1] + val)
                count += 1
        temp += 1
    if lena % 2:
        return odd[-1]/lena
    else:
        return even[-1]/lena

