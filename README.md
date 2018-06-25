# Kitābaŧ wRoutine 1.0

A simple markdown-based workflow for sustainable academic writing (with some adaptations for the field of Arabic and Islamic Studies).

## Features

- a nice, simple, yet sufficiently robust interface (<https://atom.io/>)
- atomized drafting; easy inclusion/exclusion of sections into/from the master draft;
- explicit markup through *markdown*, a simple text encoding scheme;
- images and illustrations with captions;
- cross-references to sections, images, tables within the text;
- footnotes;
- automatic citation insertion form bibliography files;
- bibliography and citation styles;
- automatic generation of desired formats (e.g., PDF, HTML, DOCX, etc.); PDF requires LaTeX engine to be installed on the machine.

The entire wRoutine is based on *markdown*; you can learn all you need to know about it from the following two tutorials on the basic principles of [*markdown*](https://programminghistorian.org/en/lessons/getting-started-with-markdown) and [*sustainable academic writing*](https://programminghistorian.org/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown).

# Requirements

The following software needs to be installed for the wRoutine to work and function properly.

- `Atom` (<https://atom.io/>), a free, hackable text editor. wRoutine is written with this text editor in mind, but it can be used with other editors as well (some features will not be available though). Desirable packages and the overall configutation is describe below.
- `Pandoc` (<https://pandoc.org/>) does all the conversion into different formats;
- `LaTeX` is used by `Pandoc` to generate PDF files; `MiKTeX`, <https://miktex.org/>, is the easiest way to install and manage `LaTeX` on any machine.

## Features for the field of Arabic and Islamic studies

These features are implemented in Atom, and require a few simple steps to be activated. They include the following:

- transliteration support, i.e. an easy insertion of tricky characters that are used for transliteration of Arabic.
- conversion of AH years into AH/CE format, which is usually used in publications.

### Transliteration Snippets for Atom

`snippets.csv` contains a table of variables to be converted into transliteration snippets for Atom. You can edit this file and add more relevant snippets.

Run `generate_snippets.py` to convert data from `snippets.csv` into the snippets format that Atom understands. These will be saved into `paste_to_snippets.cson.txt`.

The script also generates *hijri>CE* conversion data (for years only).

### Adding snippets to Atom

1. Open `paste_to_snippets.cson.txt`, select everything and copy into buffer (Ctrl+c).
2. In Atom, open `Atom > Snippets...` (this will open `snippets.scon`)
3. At the end of the file, paste (Ctrl+v) what you copied from `paste_to_snippets.cson.txt`
4. Snippets should start working immediately.

### Current configuration

#### Transliteration

1. Type `code`, then `Tab` key to insert the desired character. *NB:* there is a bit on an issue with the `Tab` key when you are trying to do that in a `list`, where `Tab` adds indentation, rather than does conversion.
2. `Codes` are organized as follows:
	1. All codes start with `,` — a comma
	2. The second character should be:
		1. `*`, `.`, or `8` for characters with `dots` (ḥ, ṭ, ḍ, ġ, etc.)
		2. `_`, or `-` for characters with macrons and breves (ā, ḫ, ḏ, ṯ, etc.)
		3. `^` for characters with `^` (š, ǧ, etc.)
	3. The third character is the desired letter (capitalized, if necessary).
	4. After that, press `Tab` to complete conversion.
3. **NB:** There are some additional characters:
	1. `,<` or `,'` for *hamzaŧ*
	2. `,>` or `,\`` for *ʿayn*
	3. `,=t` for *tāʾ marbūṭaŧ*
	4. `,~a` or `,\`a` for *ã*, *dagger alif*
	5. `,/a` for *alif maḳṣūraŧ*
	6. **EXAMPLE:** `,_a` should be converted into ā

#### *Hiǧrī* years

1. Works for the range from 1 till 1500
2. Type `,`
3. Type the desired years
4. Add `AH` (no spaces between the year and `AH`)
5. Hit `TAB`
6. **EXAMPLE:** `,748AH` should be converted into `748/1347 CE`

## Requirements





## OLD STUFF TO BE SORTED OUT

A w[riting ]routine for: 1) creating in MD and then typesetting into DOCX, HTML, PDF (all with pandoc), plus with some Islamicate flavoring along the way (betaCode conversion, AH>CE conversion, bibliography generation).

# What does one need for comfortable writing?

- a nice, but simple interface (Atom)
- explicit markup
- footnotes
- easy-to-use transliteration
- citations and bibliography management
- atomized drafting, i.e. writing in bits and pieces that can be rearranged, added/removed, and merged into a master draft
- what else?

# Update from June 16, 2018

- Project folders must begin with three undescore symbols (i.e., `___NameOfTheProject`).
- Draft can now be atomized into sections and subsections as separate files.
	- these files must be in `./draft/` subfolder of the writing project
	- in `./draft/`, you can also use subfolders for larger projects (for chapters, for example)
	- all subfolder and file names must begin with `0`; section files must end with `.md`;
	- you can ‘play’ with subfolder and file names to achieve desired order of sections in your final document, for example `000 Introduction.md` will be always before `010 Subject of the Study.md`; add a prefix `z` to exclude a section file from final draft (actually, any other prefix will work; `z.` will also push excluded section to the bottom of the list).
	- `Makefile` (i.e., running command `make` from *Terminal* [in the folder of your project]) will run all necessary conversion scripts and will generate multiple output files. More specifically:
	1. `betaCode` and AH dates are converted in all relevant files (`_generateBetaCode.py`)
	2. masterdraft is generated from sections stored in `./draft/` subfolder and saved into `_draft_autogenerated.md` (`_compile_masterDraft.py`)
	3. some final formatting is applied and bibliography file (`biblio.bib`) is updated; `main.md` file is created for conversion into other formats (`_draft_to_main.py`).
	4. [Optional] Optional means the line of code is *commented out*, you need to *uncomment* it for it to work (remove `#` in front of it)
	5. [Optional] conversion of betaCode transliteration into *Der Islam* system (`mod_translit_to_DerIslam.py`)
	6. conversion of `main.md` to PDF
	7. opening of the newly formed PDF
	8. [Optional: Lines 15-17] conversion into `.DOCX` (15), `.HTML` (16), `.TEX` (17).
- `ATOM` (<https://atom.io/>) is a great editor for this *wroutine*; on relevant settings, see *Atom Option* below, and also <http://u.arizona.edu/~selisker/post/workflow/> for more details.

## Issues

- There is some issue with `zotero_bibliography.bib` (export from my Zotero library); some fields in records must be formatted badly, since the autocomplete in Atom stops working, if this file is added as a library.
- For this reason, there is another file (`zotero_bibliography_working_with_atom.bib`) to take care of this issue; I simply add new records to that file on a need-to basis and check if it still works; **NB:** duplicate records do not cause any issues.


## Requirements

- `Pandoc` must be installed for conversion from MD to other formats (`LaTeX` must be installed for conversion to PDF; (<https://miktex.org/> is a fine installation management solution )
- `Python 3.xx`
- `make`, if not installed (installed on Mac)
- <https://atom.io/> is great for editing (not a requirement, but a very nice editor with bibliography look up; the latest version is adapted for use with `Atom`); `Atom` options are described below.

## `Atom` options

- ATOM is a nice option for an editor, particularly since it has a plugin that make auto-lookup into a bibtex file
- For settings in ATOM, see <http://u.arizona.edu/~selisker/post/workflow/>
- Bibliography file can be selected
- Themes: *UITheme*: One Light; *Syntax Theme*: Base16 Tomorrow Light (or their Dark varieties)
- `insert-timestamp` is a nice option for generating foonote numbers: with a timestamp there will not be any collisions. Python timestamp (`crtl+alt+shift+U`) would work fine for this. Example of a timestamp: `1529359692`
- *BibLatex-Check* can check the integrity of a bibTex file (my large bibliography has lots of errors, so ATOM cannot work with it)

# Older description (some valuable notes still)

## Some notes on running this thing-y

1. To run `pandoc` (easiest solution: make [Makefile]: works beautifully!)
pandoc --filter pandoc-citeproc --bibliography=biblio.bib --csl=cms-fullnote.csl -V header-includes:'\setmainfont{Brill}' --latex-engine=xelatex text.md -o text.pdf
	**Where**:
	pandoc :: the main command
  	--filter pandoc-citeproc :: enables bibliography formatting
	--bibliography=biblio.bib :: loads bibliography (bibTex file)
	--csl=cms-fullnote.csl :: uses a specific citation style (Chicago Manual of Style)
	text.md :: source file
	-o :: creates a standalone output
	text.docx :: the name of the file that will be created (doc, in this case)
	**Additional LaTeX options**:
	--V header-includes:'\setmainfont{Brill}’ :: determines the main font
	--latex-engine=xelatex :: uses xelatex, as the engine (important for Unicode)
		* Arabic requires additional tweaking of the default LaTeX template (enabling bidirectionality)

2. **The template is stored in ‘___articleCode.zip’**
	1. unzip > rename > use
	2. folders with articles must begin with "___" (3 underscores)
	3. the main text is to be kept in **_draft_articleCode.md**
		1. `make` file reformats drafts, applying betaCode, converting hijri dates, renumbering footnotes.
		2. `make` file creates **main.md** (removes comments), which is then used for typesetting other formats.
	4. bibliography in **biblio.bib** (will be generated automatically from the main bibliography file **zotero_bibliography.bib** in the main folder [one level up])
	5. Images should be copied to **../images/articleCode/**
		1. This structuring makes it easy to integrate results into a Jekyll-built website hostable on GitHub.
	6. Other files are optional

3. **Building bibliography** :
	1. Bib Keys format: **AuthorTitleYEAR[Editor]**
		1. camelCase; diacritic>simplified
		2. author :: author’s last name
		2. title :: the first word (or a keyword) from the title
		3. year
		4. [editor] :: optional, essentially only for editions of primary sources
	2. **zotero_bibliography.bib**
		1. One main bibFile exported from Zotero > all formatting changes are to be made here
		2. The file is then reformatted into a better typeset version (+ **\_mod.bib**)
		3. New bibliographical records can be added to this file
		4. Automatically reformated with a script
	4. **Bibliography for specific projects**:
		1. A script checks keys in **main.md**
		2. Then checks main bibliography file
		3. Then copies results into the relevant **biblio.bib**
	5. **make** file does the following:
		1. updates bibliography
		2. typesets DOCX
		3. typesets PDF
		4. typesets LaTeX

## Just a note on how to use  (Imagemagick)
	1. Imagemagick
		1. convert img1 img2 -append img12
			1. -append :: vertically
			2. +append :: horizontally
