# mp3nu
mp3nu (mp3 enumerator) is een programma - speciaal gemaakt voor de wonderfoon - om simpel en snel een lijst met muziek te nummeren.

Als het programma voor het eerst wordt uitgevoerd zal er in de map 'Muziek' (C:\Users\GEBRUIKER\Music) een nieuwe map worden aangemaakt, genaamd mp3nu. Deze map bevat weer twee mappen genaamd 'mp3_before' en 'mp3_after'. Als er mp3-bestanden aanwezig zijn in de 'mp3_before' map zal het programma vragen om een startnummer om vervolgens de bestanden te kopiëren en te nummeren. Het eerste nummer is hierbij het hiervoorgenoemde 'startnummer'. Bij dit proces wordt er tijdelijk een map genaamd 'mp3_temp' aangemaakt. 'mp3_temp' zal weer worden verwijderd als het programma klaar is. De genummerde mp3-bestanden komen terecht in 'mp3_after'.

Het is de bedoeling dat de 'mp3_before' map door de gebruiker wordt geleegd als het proces is voltooid. Zo wordt er voorkomen dat er dubbele bestanden ontstaan als het programma in de toekomst nogmaals wordt uitgevoerd met andere bestanden. mp3nu herkent dubbele bestanden en zal een waarschuwing geven als er in 'mp3_before' een bestand aanwezig is dat al bestaat in 'mp3_after'. Het is hierna nog mogelijk om wijzigingen te doen in 'mp3_before'.
