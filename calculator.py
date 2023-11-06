import math

def pyydaLuku():
	while True:
		luku = input("Anna luku: ")
		try:
			luku = int(luku)
			return luku
		except Exception:
			print("Virheellinen syöte!")

def laskin():
	luku1 = pyydaLuku()
	luku2 = pyydaLuku()
	while True:
		print("(1) +")
		print("(2) -")
		print("(3) *")
		print("(4) /")
		print("(5)sin(luku1/luku2)")
		print("(6)cos(luku1/luku2)")
		print("(7)Vaihda luvut")
		print("(8)Lopeta")
		print("Valitut luvut:", luku1, luku2)
		valinta = input("Tee valinta (1-8):")
		if valinta == "1":
			print("Tulos on:", luku1+luku2)
		elif valinta == "2":
			print("Tulos on:", luku1-luku2)
		elif valinta == "3":
			print("Tulos on:", luku1*luku2)
		elif valinta == "4":
			print("Tulos on:", luku1/luku2)
		elif valinta == "5":
			tulos = math.sin(luku1/luku2)
			print("Tulos on:", tulos)
		elif valinta == "6":
			tulos = math.cos(luku1/luku2)
			print("Tulos on:", tulos)
		elif valinta == "7":
			luku1 = pyydaLuku()
			luku2 = pyydaLuku()
		elif valinta == "8":
			break

def main():
	laskin()

if __name__ == "__main__":
	main()