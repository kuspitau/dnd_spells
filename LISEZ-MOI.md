# Bibliothèque locale de sorts — extension OCR (lot unique)

## Ce que contient ce dossier

**353 fiches indexées** au total : 29 fiches des deux premiers lots et **324 nouvelles fiches OCR** construites à partir du PDF de 105 pages (pages imprimées **239 à 343**).

Fichiers principaux :

- `Bibliotheque.html` : catalogue interactif autonome (recherche, filtres et survol), fonctionne directement dans Firefox hors ligne.
- `md/` : un fichier Markdown avec métadonnées YAML par sort.
- `fiches_html/` : fiches HTML/CSS individuelles (ouvrables au navigateur).
- `fiches_jpg/` : fiches longues exportées en JPEG, avec hauteur adaptée à leur contenu.
- `fiches_pdf/` : fiches PDF individuelles prêtes à imprimer.
- `Classeur_sorts.pdf` : classeur compilé A4 (360 pages, 353 signets).
- `index.json` : métadonnées structurées et descriptions des sorts.
- `source_pages/` : 105 scans JPEG des pages imprimées 239 à 343 pour permettre le contrôle des transcriptions.
- `controle_extraction.csv` : index des fiches et de leur niveau de vérification.
- `revue_prioritaire.csv` : anomalies OCR détectées automatiquement ; à utiliser pour concentrer la relecture.
- `progression.json` : état et traçabilité des lots.
- `spells_auto.json` : **source des 324 nouvelles transcriptions OCR**, distincte des 29 transcriptions précédentes contenues dans `spells_data.py` et `spells_lot2.py`.

## Mise à jour du projet existant

Décompresser le ZIP **dans le dossier parent** de votre répertoire `Bibliotheque_sorts/`. L'archive contient elle-même le préfixe `Bibliotheque_sorts/` : accepter la fusion des dossiers et le remplacement des fichiers portant le même nom (`Bibliotheque.html`, `index.json`, `Classeur_sorts.pdf`, scripts et rapports). Les 29 fiches précédentes ne sont pas supprimées ; le ZIP livre principalement les 324 fiches ajoutées et les fichiers de catalogue actualisés.

Si le dossier existant porte un autre nom, adapter le nom du dossier de l'archive avant extraction ou fusionner manuellement les répertoires correspondants.

## Important — fidélité des textes

**Ce lot est un inventaire OCR utilisable mais PAS une transcription intégralement vérifiée.** Les 324 nouvelles fiches portent `statut: ocr_non_valide`. La couche texte du PDF est de mauvaise qualité : la reconnaissance de colonnes, des encadrés, des tableaux, des caractéristiques de créatures et des suites sur plusieurs pages reste faillible. Plusieurs entrées ont été ajoutées/corrigées manuellement depuis les images, mais une vérification complète (valeurs numériques, formulation et présence de tous les sorts) n'a pas été réalisée.

Les principaux risques résiduels sont : fautes OCR (1/l, d/0, accents), noms ou champs inexacts, descriptions incomplètes, tableaux ou profils de créatures mal reconstruits, et **éventuels sorts non détectés**. Il faut comparer la fiche au scan original avant de s'appuyer sur un sort pour arbitrer une règle. Les scans sources sont accessibles depuis chaque fiche HTML et depuis le bas des Markdown OCR. L'existence d'une fiche JPG n'est pas une preuve de validation du contenu.

**N'utilisez pas le nombre 353 comme preuve d'exhaustivité du chapitre.** Il représente uniquement les entrées indexées à ce stade.

## Génération et personnalisation

Pour reconstruire l'index, les Markdown et les pages HTML à partir des sources Python et JSON :

```bash
pip install -r requirements.txt
python build_library.py
```

Pour recréer les JPG et PDF, installer Playwright et Chromium local, puis lancer `python export_jpg.py`. Le script utilise actuellement Chromium à l'emplacement `/usr/bin/chromium` (adapter ce chemin sous Windows si besoin). Les PDF individuels et les JPEG livrés peuvent être consultés **sans installer Python**.

Le répertoire `illustrations/` conserve les illustrations associées à certaines fiches du prototype ; les légendes illustratives ne doivent pas être prises pour du texte de règles.
