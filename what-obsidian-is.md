# What Obsidian Is

Open almost any other note-taking app
and your notes live inside it: stored
in its database, on its company's
servers, in a shape only that program
can read. If the company changes its
prices, its mind, or its existence,
your notes negotiate with it for their
release. People have lost years of
notes that way, politely, at the end
of a sunset announcement.

**Obsidian** inverts the arrangement.
Your notes are files — plain text in
**Markdown**, one file per note, in an
ordinary folder on your own disk.
That folder is called a **vault**.
Obsidian is a program you point at a
vault: an **editor** that reads the
folder, shows the notes nicely, and
adds the things a folder of text files
cannot do for itself — clickable links
between notes, a list of what links to
what, fast search, templates, and a
map of the connections. Uninstall
Obsidian tomorrow and the vault is
still there, complete, readable in any
text editor ever made. This guide's
lab proves that more than once: every
check in chapters 2, 5 and 7 is run on
the vault with no app involved at all.

## The shape of it

Three facts explain nearly everything
in this guide:

- **The files are the notes.** There
  is no database of your words. An
  edit in Obsidian is an edit to a
  file; an edit to the file in another
  editor is an edit Obsidian sees when
  it next looks. Chapter 2 takes the
  folder apart.
- **Links are text.** A link from one
  note to another is a few characters
  typed inside the note itself —
  `[[Tomatoes]]` in the style Obsidian
  grew up with, or an ordinary
  Markdown link. Chapter 5 shows what
  each style points at, and the lab's
  experiments show what breaks each.
- **The app keeps its own notebook
  separate.** Obsidian's settings for
  a vault live in a hidden subfolder,
  `.obsidian`, and they are settings —
  not your words. Deleting them resets
  the app's manners, not your notes.

## The rules, stated before everything else

A vault is closer to a diary than to a
document folder. It holds half-formed
thoughts, drafts, records — the raw
material of somebody's thinking, kept
precisely because it is private. So
this guide has rules, and they are not
fine print:

> **Your notes are yours.** Treat every
> copy of a vault — a sync service, a
> backup, a laptop left logged in — as
> a copy of the diary, and decide who
> holds it on that basis.

> **A plugin is somebody else's
> program.** Community plugins
> (chapter 13) run inside the app with
> your notes in reach. That can be
> wonderful. It is still handing a
> stranger's code the run of the
> diary, and it deserves the care you
> would give a house key.

> **If the notes are not yours, their
> owner's rules rule.** A vault of a
> client's or an employer's material
> may not live wherever your own may,
> whatever this guide says about your
> own.

The lab obeyed the strictest version:
its vault is entirely invented, its
app never signed in, never synced,
and was never given a real note to
read. Yours can be exactly as private:
nothing in the next eighteen chapters
needs an account until the optional,
paid extras in chapters 11 and 14.

## Who makes it, and what it costs

Obsidian is made by a small company,
Dynalist Inc., and the app itself is
**proprietary** — closed source, a
fact chapter 17 weighs honestly
against the openness of the files.
The app is free to download and use,
for personal purposes and, since
2025, for work as well; a paid
commercial licence survives as an
optional way for companies to support
it. The company earns its money from
optional add-ons instead: **Sync**,
its end-to-end encrypted syncing
service (chapter 11), and **Publish**,
which turns notes into a website
(chapter 14), plus a **Catalyst**
licence that buys early-access builds
and a warm feeling. None of those is
needed to follow this guide.

Check: you can state the model in one
sentence — *Obsidian is an editor
over a folder of plain files, and the
folder is the notes.* The lab's first
transcript, `obsidian-lab/transcripts/t00-vault-tree.txt`,
is that sentence as a directory
listing: nine small text files and a
picture, nothing else.

## What it is not

Obsidian is not a word processor: it
writes Markdown, and pretty documents
are other tools' country. It is not a
team wiki: one writer at a time is
its natural state (chapter 17). It is
not a backup: a vault on one disk is
exactly as safe as that disk, and
chapter 11 is about copies, not
comfort. And it is not magic: the map
in chapter 6 is drawn from the links
you typed, and knows nothing you did
not tell it.
