from fastapi import FastAPI, HTTPException

app = FastAPI()
public_key = 7
private_key = 3

def encrypt(message):
    return (message ** public_key) % 33

def decrypt(ciphertext):
    return (ciphertext ** private_key) % 33

@app.get("/encrypt/{message}")
async def encrypt_message(message: int):
    encrypted_message = encrypt(message)
    print("Encrypted message:", encrypted_message)
    return {"encrypted_message": encrypted_message}

@app.post("/decrypt")
async def decrypt_message(ciphertext: int):
    decrypted_message = decrypt(ciphertext)
    print("Decrypted message:", decrypted_message)
    return {"decrypted_message": decrypted_message}
