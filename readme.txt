
checksum_tester 
----------------

-> durchsucht alle Unter-Verzeichnisse von Verzeichnis_1 und vergleicht dessen Dateien (& Verknüpfungen) mit den 
			       Dateien von Verzeichnis_2 anhand ihrer Hash-Werte 

-> zeigt Summe aller identischen Files (mit identischen Hash-Werten) gegenüber der GesamtAnzahl aller Files 

-> legt log-files an zu veränderten oder korrupted Files (unterschiedliche Hash-Werte derselben Datei), 
		     zu gelöschten, verschobenen oder umbenannten Files (nicht-existent) 
		 und zu neu-erstellten Files (ohne Äquivalent im anderen Datensatz) 
		(wobei zwischen den letzten beiden Gruppen Überschneidungen entstehen können, die das Programm nicht sauber 
		 herausstellt -> diese können nur optischen mithilfe der log-files identifiziert werden) 

-> geignet für den Abgleich zweier Datensätze mit stark ähnlichem Verzeichnis-Baum 
	(bspw. AusgangsDatensätze mit wiederhergestellten Daten, Backups etc.) 