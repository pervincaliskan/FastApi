import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
i = 10  # Toplam alınacak sayının üst sınırı
result = proxy.toplam(i)
print(f"0'dan {i}'e kadar olan sayıların toplamı: {result}")
