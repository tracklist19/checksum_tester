
checksum_tester 
----------------

-> durchsucht alle Unter-Verzeichnisse von Verzeichnis_1 und vergleicht dessen Dateien (inkl. Verknüpfungen) mit den 
			       				Dateien von Verzeichnis_2 anhand ihrer Hash-Werte (SHA-256), 
						zusätzlich danach: Gegen-Vergleich um neu-erstellte, verschobene oder umbenannte in Verzeichnis_2 zu identifizieren  

-> zeigt Summe aller identischen Files (mit identischen Hash-Werten) gegenüber der GesamtAnzahl aller Files 

-> legt log-files an zu veränderten oder korrupten Files (unterschiedliche Hash-Werte derselben Datei), 
		     		 zu gelöschten, verschobenen oder umbenannten Files (nicht-existent in Verzeichnis_2) 
		 		 und zu neu-erstellten Files (ohne Äquivalent im anderen Datensatz) 
			(wobei zwischen den letzten beiden Gruppen Überschneidungen entstehen können, die das Programm nicht sauber 
		 	 herausstellt -> diese können nur optischen mithilfe der log-files identifiziert werden) 

-> allgemein geeignet für den Abgleich zweier Datensätze mit stark ähnlichem Verzeichnis-Baum 
		(bspw. Vergleich AusgangsDatensätze mit wiederhergestellten Daten, Backups etc.) 



