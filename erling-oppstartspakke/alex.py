print("ERLING OG TEAMET")
print("Etter seks uker begynner ulike faglige perspektiver å kollidere.")
print("Prototypen skal vises om tre uker. Erling må hjelpe teamet gjennom storming-fasen.\n")

print("1. Hvordan bør Erling håndtere konflikten mellom Silje og Elias?")
print("A) Ha enesamtaler og deretter et strukturert fellesmøte.")
print("B) Skjære gjennom og avgjøre teknologivalget med en avstemning.")
valg1 = input("Velg A eller B: ").strip().upper()
while valg1 != "A" and valg1 != "B":
    print("Ugyldig svar. Skriv A eller B.")
    valg1 = input("Velg A eller B: ").strip().upper()

if valg1 == "A":
    print("Erling hjelper dem med å skille sak fra person. Tilliten bevares, men møtene tar tid.\n")
else:
    print("Avgjørelsen kommer raskt. Silje føler seg overkjørt og trekker seg fra samarbeidet.\n")

print("2. Hvordan bør Erling håndtere uenigheten om innbyggerdialog?")
print("A) Arrangere en workshop og prøve ut en liten testpilot med brukere.")
print("B) Utsette diskusjonen for å spare tid fram mot prototypen.")
valg2 = input("Velg A eller B: ").strip().upper()
while valg2 != "A" and valg2 != "B":
    print("Ugyldig svar. Skriv A eller B.")
    valg2 = input("Velg A eller B: ").strip().upper()

if valg2 == "A":
    print("Hamdi og Hallgeir får fram behovene sine. Teamet bruker ekstra tid, men bygger felles forståelse.\n")
else:
    print("Teamet sparer tid nå, men Hallgeir føler seg oversett og frustrasjonen blir liggende.\n")

print("3. Det er én uke igjen. Hvordan leder Erling innspurten?")
print("A) Legge vekt på relasjoner, korte innsjekker og feiring av delmål.")
print("B) Styre oppgavene stramt og rette oppmerksomheten mot fristen.")
valg3 = input("Velg A eller B: ").strip().upper()
while valg3 != "A" and valg3 != "B":
    print("Ugyldig svar. Skriv A eller B.")
    valg3 = input("Velg A eller B: ").strip().upper()

if valg3 == "A":
    print("Teamet får støtte og beholder motivasjonen, men mindre tid går direkte til produksjon.")
else:
    print("Arbeidet går raskere framover på kort sikt, men presset svekker motivasjonen.")

# Sluttutfallet bestemmes av de tre valgene.
antall_a = 0
if valg1 == "A":
    antall_a = antall_a + 1
if valg2 == "A":
    antall_a = antall_a + 1
if valg3 == "A":
    antall_a = antall_a + 1

print("\nSLUTT")
if antall_a == 3:
    print("Erling har prioritert dialog og tillit. Teamet finner felles normer og går mot norming-fasen.")
    print("Prototypen blir forsinket, men samarbeidet står sterkere.")
elif antall_a == 0:
    print("Erling har prioritert raske avgjørelser og utsatt vanskelige samtaler.")
    print("Tilliten svekkes, og teamet blir stående i storming-fasen.")
else:
    print("Erling har håndtert noen utfordringer, mens andre spenninger blir liggende.")
    print("Teamet får framdrift, men samarbeidet er sårbart.")