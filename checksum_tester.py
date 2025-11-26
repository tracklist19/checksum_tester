
### readme.txt siehe _nfo_checksum_tester.txt 
### funktioniert solang die Größe der zu hashenden File  
	## nicht die Größe des verfügbaren/freien ArbeitsSpeichers [RAM] übersteigt 
	## sonst throwt Python MemoryError oder Programm stürzt ab [OOM-Kill] 
	## sicherer: Files chunk-weise hashen mit Hash-Funktion, siehe unten 


import glob
import os
import hashlib


###  PATHS 

src = input("source path [lastBU]: \n")
trg = src.replace(r"M:\lastBU", r"N:\latestData")						# replace if possible, otherwise: input("target path [latest/recoveredData]: \n")
log_path = r"L:\logs"

path_list_src = glob.glob(src + '/**/*', recursive=True)
path_list_trg = glob.glob(trg + '/**/*', recursive=True)



###  GET HASHES

print("\n\nCHECK lastBackup [src] AGAINST latest/recoveredData [trg]\n")

cnt_ges_src = 0 														# Zähler_gesamt für src
cnt_hash = 0															# Zähler Hash=identical
cnt_cc_src = 0	 														# Zähler changed/corrupted für src
cnt_dmr_src = 0	 														# Zähler deleted/moved/renamed für src

for p_src in path_list_src: 
	## File or Link, not Dir
	if os.path.isfile(p_src) or os.path.islink(p_src):
		cnt_ges_src += 1
	## get equivalentPath in latest/recoveredData
		print("\n" + p_src)
		p_trg = p_src.replace(r"M:\lastBU", r"N:\latestData")
		print(p_trg)
	## compare hashes
		if os.path.isfile(p_trg) or os.path.islink(p_trg):
			hash_src = hashlib.sha256(open(p_src,'rb').read()).hexdigest()
			hash_trg = hashlib.sha256(open(p_trg,'rb').read()).hexdigest()
			print(hash_src)
			print(hash_trg)
			if hash_src == hash_trg: 
				print("Files are identical.")
				cnt_hash += 1
			if hash_src != hash_trg: 
				print("Files are not identical: Changed or Corrupted.")
				cnt_cc_src += 1
				with open(log_path + '\log_ChangedCorruptedFiles.txt', "a", encoding="utf-8") as f1:
					f1.write("\n" + p_src)
		else:
			print("File not found: Deleted or Moved or Renamed.")
			cnt_dmr_src += 1
			with open(log_path + '\log_DeletedMovedRenamedFiles.txt', "a", encoding="utf-8") as f1:
				f1.write("\n" + p_src)

	## write counter
with open(log_path + '\log_ChangedCorruptedFiles.txt', "a", encoding="utf-8") as f1:
		f1.write("\n\n\n---------- \nChangedCorruptedFiles \n---------- \nlastBackup [src] against recoveredData [trg] \n----------\n" \
				 "\n\nChangedCorrupted:    " + str(cnt_cc_src) + " / " + str(cnt_ges_src) \
			   + "\nDeletedMovedRenamed: " + str(cnt_dmr_src) + " / " + str(cnt_ges_src) \
			   + "\nHash=identical:      " + str(cnt_hash) + " / " + str(cnt_ges_src) \
			   + "\nSUM_all_src:         " + str(cnt_cc_src+cnt_hash+cnt_dmr_src) + " / " + str(cnt_ges_src) \
			   + "\ncnt_all_winEig:             ")
with open(log_path + '\log_DeletedMovedRenamedFiles.txt', "a", encoding="utf-8") as f1:
		f1.write("\n\n\n---------- \nDeletedMovedRenamedFiles \n---------- \nlastBackup [src] against recoveredData [trg] \n----------\n" \
			     "\n\nChangedCorrupted:    " + str(cnt_cc_src) + " / " + str(cnt_ges_src) \
			   + "\nDeletedMovedRenamed: " + str(cnt_dmr_src) + " / " + str(cnt_ges_src) \
			   + "\nHash=identical:      " + str(cnt_hash) + " / " + str(cnt_ges_src) \
			   + "\nSUM_all_src:         " + str(cnt_cc_src+cnt_hash+cnt_dmr_src) + " / " + str(cnt_ges_src) \
			   + "\ncnt_all_winEig:             ")



###  CHECK NEU-ERSTELLTE (/VERSCHOBENE/RENAMED)							# auf trg

print("\n\nCHECK latest/recoveredData [trg] AGAINST lastBackup [src]\n")

cnt_ges_trg = 0 														# Zähler_gesamt für trg
cnt_cmr_trg = 0															# Zähler created/moved/renamed für trg

for p_trg in path_list_trg: 
	## File or Link, not Dir
	if os.path.isfile(p_trg) or os.path.islink(p_trg):
		cnt_ges_trg += 1
	## get equivalentPath in lastBackup
		print("\n" + p_trg)
		p_src = p_trg.replace(r"N:\latestData", r"M:\lastBU")
		print(p_src)
	## find new/moved/renamed files
		if not os.path.isfile(p_src) or os.path.islink(p_src):
			print("File not found: newly Created or Moved or Renamed.")
			cnt_cmr_trg += 1
			with open(log_path + '\log_newlyCreatedMovedRenamedFiles.txt', "a", encoding="utf-8") as f1:
				f1.write("\n" + p_trg)
		else:
			print("File found.")										# die beidseitig-vorhandenen Files mit unterschiedl.Hashes [ChangedCorruptedFiles] sind hier mit enthalten, werden aber hier nicht separat ausgewiesen

	## write counter
with open(log_path + '\log_newlyCreatedMovedRenamedFiles.txt', "a", encoding="utf-8") as f1:
	f1.write("\n\n\n---------- \nnewlyCreatedMovedRenamedFiles \n---------- \nrecoveredData [trg] against lastBackup [src] \n----------\n" \
		     "\n\nChangedCorrupted:         " + str(cnt_cc_src) + " / " + str(cnt_ges_trg) \
		   + "\nnewlyCreatedMovedRenamed: " + str(cnt_cmr_trg) + " / " + str(cnt_ges_trg) \
		   + "\nHash=identical:           " + str(cnt_hash) + " / " + str(cnt_ges_trg) \
		   + "\nSUM_all_trg:              " + str(cnt_cmr_trg+cnt_hash+cnt_cc_src) + " / " + str(cnt_ges_trg) \
		   + "\ncnt_all_winEig:                  ")						# neuErstellte/Moved/Renamed_Files in trg PLUS die beider mit identischen & nicht-identischen [ChangedCorruptedFiles] Hashes müssen zusammen die GesamtAnzahl an Files in trg ergeben


input("\n\nZum Beenden beliebige Taste drücken...")






########################################################################


"""

HASH-FUNKTION : zum chunk-weise hashen der Files 
-------------------------------------------------

def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()
    
    
 ab Python 3.11 auch einfacher mit file_digest() : 
 --------------------------------------------------

with open(fname, "rb") as f:
	digest = hashlib.file_digest(f, "sha256")
	print(digest.hexdigest())


"""

########################################################################
