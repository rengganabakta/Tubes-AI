import random

beginning_inventory = 100
shift_tambahan = 0

def generate_permintaan():
    dadu = random.randint(1, 6)
    if dadu == 1:
        return 80
    elif dadu == 2:
        return 90
    elif dadu == 3:
        return 100
    elif dadu == 4:
        return 110
    elif dadu == 5:
        return 120
    else:
        return 130

# Simulasi harian
for hari in range(1, 101):  # asumsi 365 hari kerja dalam satu tahun
    permintaan = generate_permintaan()
    ending_inventory = beginning_inventory + 100 - permintaan
    if ending_inventory <= 50:
        shift_tambahan += 1
    beginning_inventory = ending_inventory

print("Perkiraan shift tambahan yang diperlukan:", shift_tambahan)
