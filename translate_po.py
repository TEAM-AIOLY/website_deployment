from googletrans import Translator
from pathlib import Path
import polib

# Chemin vers ton fichier .po
po_path = Path("locale/en/LC_MESSAGES/django.po")

po = polib.pofile(po_path)
translator = Translator()

for entry in po.untranslated_entries():
    if entry.msgid.strip():
        translation = translator.translate(entry.msgid, src='fr', dest='en')
        entry.msgstr = translation.text
        entry.msgid = entry.msgid.strip()
        print(f"✅ {entry.msgid} → {entry.msgstr}")

po.save(po_path)
print("Traduction automatique terminée ✅")