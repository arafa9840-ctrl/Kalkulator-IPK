def hitung_ipk(nilai, sks):
    total = sum(n*s for n, s in zip(nilai,sks))
    return total / sum(sks)

print(hitung_ipk([4, 3.5, 4], [3, 2, 3]))