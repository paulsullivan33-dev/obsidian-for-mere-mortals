# Obsidian for Mere Mortals

Most note-taking apps keep your notes
in *their* cupboard: a database on their
servers, in a shape only their program
can open. **Obsidian** works the other
way round. Your notes are a **vault** —
an ordinary folder on your own disk,
full of ordinary **Markdown** files,
one per note. Obsidian is an **editor**
that sits on top of that folder and
adds the conveniences a folder cannot
give itself: links between notes that
you can follow with a click, a list of
everything that links back, search,
templates, and a map of how the notes
connect.

This guide explains how that works, how
to open a folder as a vault and write
your first notes, the two ways of
linking notes together and what breaks
each of them, the panel that shows who
links to the note you are reading, the
**properties** and **tags** that turn
loose notes into something you can
query, and the honest questions to ask
before you let the folder be copied
anywhere else — because the limits are
stated plainly here, including the big
one: the app is a guest in the folder,
and everything it knows, it learned
from files you can read without it.

The rules that govern everything here
are stated in chapter 1 and repeated
where they bite: **your notes are
yours** — a vault is a private record
of your thinking, and every copy of it
is a privacy decision; and **a plugin
is somebody else's program** running
with your notes in reach, so you
install one the way you would hand
over a house key, not the way you
click an advertisement.

The lab behind this guide ran the real
thing two ways. First it built a small
fictional vault — a gardener's
notebook, nine notes, twenty-six
links, one picture — using nothing but
a text editor and ordinary file
commands, and proved from the files
alone which links resolve, what a
rename breaks and what a move does
not. Then it downloaded **Obsidian
1.14.5**, the official AppImage,
launched it on a virtual screen in the
same sandbox, and opened a copy of
that very vault. The app read the
files as they lay: its explorer listed
every note, its properties panel
understood the gardener's data as
data, its backlink counter agreed
with the lab's own count, and its
graph drew the same nine notes. When
it closed, the notes on disk were
byte for byte what they had been
before it opened them. The only thing
it added was a settings folder of its
own — which this guide then read with
a plain JSON parser, because that is
the point: there is no cupboard.

What the lab could not do, it did not
fake. It never signed in, so Obsidian
Sync, Publish, and the account side of
the app are taught from the
documentation and labelled as such.
Community plugins were not installed —
the sandbox app had no network it
could be trusted with, and chapter 13
explains why that caution is the
chapter, not a gap in it. The popular
Dataview plugin and the newer Bases
feature are given an honest outline in
chapter 14, not a worked lab.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What Obsidian is**](what-obsidian-is.md) —
  an editor over a folder of files,
  what that buys you, and the two
  rules that govern everything after
- [**The vault**](the-vault.md) —
  what a vault is on disk, what lives
  in the `.obsidian` folder, and what
  is simply your files
- [**Installing Obsidian**](installing-obsidian.md) —
  the installers, the first launch,
  and opening a folder as a vault
- [**Your first notes**](your-first-notes.md) —
  writing Markdown in the editor,
  reading and editing views, and
  keeping the files honest
- [**Links**](links.md) — wikilinks
  and Markdown links, what each one
  points at, and what breaks each —
  with the lab's rename and move
  experiments as the proof
- [**Backlinks and the graph**](backlinks-and-the-graph.md) —
  who points at this note, the local
  and global graphs, and an honest
  word about what the graph is for
- [**Properties and tags**](properties-and-tags.md) —
  YAML front matter the app reads as
  data, property types, and tags in
  the text and on the note
- [**Finding things**](finding-things.md) —
  full-text search with operators,
  the quick switcher, and bookmarks
- [**Templates and daily notes**](templates-and-daily-notes.md) —
  stamping out notes with the shape
  filled in, and a note a day
- [**Attachments**](attachments.md) —
  pictures and files inside notes,
  embeds, and where the files land
- [**Keeping a vault in step**](keeping-a-vault-in-step.md) —
  Sync, git, and file-sync tools
  compared plainly, with the privacy
  of each stated, and what conflicts
  look like
- [**Core plugins**](core-plugins.md) —
  the thirty built-in features, which
  are on, and what the useful ones do
- [**Community plugins**](community-plugins.md) —
  other people's code in your vault:
  restricted mode, choosing carefully,
  and the safety rule
- [**Dataview, Publish and Bases**](dataview-publish-and-bases.md) —
  querying your notes like a database,
  publishing them as a website, and
  table views over properties — in
  outline, and labelled as such
- [**Recipes**](recipes.md) — a season
  log, an inventory that stays honest,
  and a weekly review, all from the
  lab's garden notebook
- [**The neighbours**](the-neighbours.md) —
  Logseq, Notion, and a plain folder
  of text files: what each does with
  your notes that Obsidian doesn't,
  and vice versa
- [**Limits**](limits.md) — a closed
  app over open files, the graph's
  temptation, sync conflicts, and
  what no plugin can fix
- [**Troubleshooting**](troubleshooting.md) —
  the red link, the missing picture,
  the properties that will not show,
  and the empty vault that is really
  the wrong folder
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Turning a vault into a public website
beyond the outline of Publish in
chapter 14, building community
plugins, and the paid tiers in
shopping-guide detail. Sharing a
vault with a team in real time —
Obsidian is a one-writer-at-a-time
tool at heart, and chapter 17 says
why that is a limit, not a setting.
Other people's notes: a vault you are
handed is still their private record,
and the rules in chapter 1 apply to
it exactly as to your own.

## How to use this guide

Read chapter 1 for the model and the
rules, and chapter 2 before creating
anything — knowing which part of the
folder is yours and which part is the
app's settings turns later confusion
into a named problem. Chapters 3 and
4 get a first vault open and a first
note written in one sitting. Chapter
5 is not the optional chapter:
understand what a link points at
before you have five hundred of them,
because the rename experiment in that
chapter is painless at nine notes and
a small archaeology project at nine
hundred. The lab's vault lives in
`obsidian-lab/vault/` — copy it, open
it, break its links and fix them;
its transcripts are in
`obsidian-lab/transcripts/`, its
checking scripts in
`obsidian-lab/scripts/`, and its
notes in `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Markdown for Mere Mortals](https://paulsullivan33-dev.github.io/markdown-for-mere-mortals/)
- [BookStack for Mere Mortals](https://paulsullivan33-dev.github.io/bookstack-for-mere-mortals/)
- [MkDocs for Mere Mortals](https://paulsullivan33-dev.github.io/mkdocs-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/obsidian-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/obsidian-for-mere-mortals/blob/main/LICENSE-CODE).
