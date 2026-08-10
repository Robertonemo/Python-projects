import qrcode
data = input("Enter the data to encode in the QR code: ").strip()
qr = qrcode.make(data)
filename = input("Enter the filename to save the QR code: ").strip()
qr.save(filename + ".png")
print(f"QR code generated and saved as {filename}.png")