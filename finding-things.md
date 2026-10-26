# Finding Things

Outcome: in a vault of any size you
can get to a note three ways — by
searching its words, by jumping to
its name, or by having marked it in
advance — and you understand what
each way is actually looking at.

## Search: the words themselves

The **search** panel (a core plugin,
chapter 12) searches the text of
every note in the vault. It is
literal: it finds the words you
typed, as you typed them, and chapter
17 will hold it to that. Around the
plain box sit **operators** that
sharpen a search from a haystack to
a handful:

- `"rain counts"` — the exact phrase,
  in quotes.
- `tag:#crop` — notes carrying a tag;
  `file:seed` — notes whose *name*
  matches; `path:"Daily Notes"` —
  notes in a folder.
- `-compost` — exclude a word; the
  minus is how big vaults stay
  searchable.
- Capital `OR` and grouping
  brackets, for the searches that
  need them.

Results show the matching lines with
their surroundings, grouped by note,
with counts. Two habits matter more
than the operators: search before
you create (the note you are about
to write may exist under a cousin's
name, and two half-notes are worse
than either), and search your own
*rules* — status words, tag names —
when a vault feels messy, because
the mess is usually a rule quietly
forked into two spellings.

The words are the index. Nothing in
this chapter needs the app to have
built anything secret: the lab found
every mention of *compost* in its
vault with a plain text search from
the command line
(`obsidian-lab/transcripts/t05-tags-and-text.txt`),
and the app's panel is that search
with better manners and a memory for
operators.

## The quick switcher: by name

Search asks *what says this*; the
**quick switcher** asks *take me to
the note called…* Press its shortcut
(Ctrl or Cmd + O in the default
setup), type a few letters of a
name, and jump. It is fuzzy — `tmto`
finds Tomatoes — and it learns which
notes you visit, so the vault's real
hubs float to the top. In a vault
past a hundred notes this is the
door you will use most, and it is
why chapter 4 nagged about names: a
note named for its subject is a note
the switcher can find from three
letters and a hunch.

## Bookmarks: the marked few

**Bookmarks** (also core) are the
third way: notes, searches, even
graphs you have marked in advance,
kept in a panel and in a file,
`bookmarks.json`, in — of course —
`.obsidian`. A front door note
(chapter 4), the current project,
the standing search for
`status: growing`: a handful is a
tool, a hundred is just the vault
again with stars on. Bookmarks are
per vault and they travel with the
settings, which chapter 11 will
remind you is both their convenience
and their catch when two machines
disagree about what was marked.

Check: in the lab vault, search for
`status` — the hits are the word
sitting in the front matter of
`Tomatoes.md` (`status: growing`)
and of the crop record template
(`status: planned`), because
properties are text and search reads
text. Then
search `tag:#crop`. Two different
questions, both answered from the
same nine files: which is the whole
argument of this guide, arriving on
schedule.
