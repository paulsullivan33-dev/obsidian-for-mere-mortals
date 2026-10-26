# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's vault is an invented gardener's notebook.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 17 names what the tool
   cannot do: a closed-source app standing over open files,
   a graph that maps links without understanding them, search
   that finds words and not meaning, one writer at a time,
   and notes that are only as private as the copies made of
   them.
8. **The privacy rule is in the text, early.** Chapter 1 and
   the README state the rules plainly — *your notes are
   yours; a plugin is somebody else's program; every copy is
   a privacy decision* — before any procedure depends on
   them, and chapters 11 and 13 return to them where sync
   and plugins make the choice real.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox.
The lab worked at two layers. At the file layer it built a
fictional vault — a gardener's notebook of nine Markdown
notes, twenty-six links and one PNG — with a text editor and
ordinary file commands, and checked it with two small Python
scripts kept in `obsidian-lab/scripts/`. At the app layer it
downloaded the official **Obsidian 1.14.5** Linux AppImage,
extracted it (the sandbox has no FUSE), ran it on a virtual
X display (Xvfb) with a throwaway HOME, and opened a copy of
the same vault in it. Transcripts live in
`obsidian-lab/transcripts/`.

Run for real, with transcripts as evidence:

- The vault as files: the full tree and sizes (t00), and a
  link checker applying the two link styles' rules from the
  files alone — 9 notes, 26 links, all resolving (t01).
- The rename experiment on a scratch copy: renaming
  `Tomatoes.md` by hand broke 6 links — five wikilinks that
  name it and one Markdown link that paths to it (t03).
- The move experiment on a scratch copy: moving `Compost.md`
  into a new `Beds/` folder broke exactly 1 link — the
  path-based Markdown link in `Home.md` — while every
  name-based wikilink survived (t04).
- Tags and text found with grep, no app involved, and the
  embedded picture shown to be a file on disk (t05).
- Properties parsed by a plain YAML parser (a `sown` value
  arriving as a real date, not a string), and the app's
  `.obsidian` settings parsed by a plain JSON parser —
  `core-plugins.json` alone accounting for all thirty core
  plugins (t06).
- The app itself, at 1.14.5 (t07): the launcher and its
  version; "Open folder as vault" on a copy of the lab
  vault; the explorer listing all nine notes; `Home.md`
  rendered with both link styles shown as links and a
  status bar reading "2 backlinks"; `Tomatoes.md` rendered
  with its properties panel (type, status, a date, bed) and
  "6 backlinks, 4 properties" — 6 being exactly the count
  the file-layer checker reports for links to that note;
  the graph view drawing all nine notes; a `.obsidian`
  folder written by the app into the vault (app, appearance,
  core-plugins and workspace files at first, `graph.json`
  after the graph was opened); and, after closing, a diff
  proving the app changed no note — the vault's notes were
  byte for byte identical, `.obsidian` the only addition.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Obsidian Sync, Publish, Catalyst and the commercial
  licence: no account was created and nothing was bought,
  so the whole account side of the app is documented-only.
- Community plugins: none was installed. The lab app had an
  intercepted network and was given no account; chapter 13
  teaches the selection and safety discipline from the
  documentation and the plugin model's plain facts.
- Dataview's query language and Bases' view definitions
  (chapter 14): outlined, not exercised. Bases' presence as
  a core feature in 1.14.5 is itself verified — it is listed
  in the `core-plugins.json` the app wrote, and its "New
  base" button appeared on the lab's new-tab page.
- Mobile apps (Android, iOS): not run; the desktop Linux app
  is the verified surface.
- git-based sync of a vault (chapter 11): the comparison is
  from the tools' documentation; the file-sync behaviour it
  contrasts with is the lab's own file handling.
- The comparison tools in chapter 16 are characterised, not
  benchmarked; Logseq and Notion were not installed.
- The AppImage's startup update check failed in the sandbox
  with a certificate error caused by the build machine's
  intercepted network — recorded in t07 so nobody mistakes
  it for app or vault behaviour.

Fixtures are this guide's own and deliberately generic: a
fictional gardener, three beds, six tomato plants of a
variety that does not exist, and a garden plan drawn by a
thirty-line script in the lab. No example is modelled on
any real person, garden, organisation or set of notes, and
the vault's `.obsidian` folder is the one the real app
wrote into the lab's own copy, carried across unchanged.
