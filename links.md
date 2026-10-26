# Links

Outcome: you can link two notes in
either of the two styles, say exactly
what each style points at, and
predict — before it happens to a
vault you care about — what a rename
breaks and what a move does not. The
lab's experiments are the proof, and
they are small enough to repeat on
the lab vault in five minutes.

## Why links are the whole game

A folder of notes is a pile. Links
make it a **notebook**: the tomato
note names the compost heap, the
compost note names the tomatoes back,
and following those threads is most
of how you will actually read what
you wrote. Every later feature —
backlinks, the graph, half of search
— is bookkeeping over the links you
type. So they repay one careful
chapter.

## Wikilinks: pointing by name

The style Obsidian grew up with is
the **wikilink**, double brackets
around a note's name:

```markdown
They are fed from the [[Compost]] heap.
```

A wikilink points by **name**. It
does not say where the note lives;
it says what it is called, and the
app finds a note of that name
anywhere in the vault. Around that
simple core sit the useful variants,
all still just text in the file:

- `[[Compost|the heap]]` — show
  *the heap*, point at `Compost`.
  The part after the `|` is a
  **display alias**, cosmetics only.
- `[[Garden Map#North bed]]` — point
  at a **heading** inside the note,
  not just the note.
- `[[Tomatoes#^some-id]]` — point at
  one marked **block** of text, for
  the rare link that must land on a
  paragraph. Rare is right; headings
  carry most of the load.

And a wikilink to a note that does
not exist yet is an **unresolved
link**: shown dimmed or in another
colour, kept in the bookkeeping, and
clicking it creates the note. It is
chapter 4's promise-keeping, and it
is a feature, not damage.

## Markdown links: pointing by path

The older, universal style is the
**Markdown link**:

```markdown
The compost notes are kept as
[a plain Markdown link](Compost.md).
```

A Markdown link points by **path** —
the file's address relative to the
note doing the linking (here, "the
file `Compost.md` in this same
folder"). Every Markdown tool on earth
understands it, including the ones
that render this guide's own pages.
Obsidian reads and follows both
styles, and a setting (**Files &
Links → Use [[Wikilinks]]**) chooses
which style the app itself writes
when you link by dragging or
completing. The lab vault deliberately
keeps a few Markdown links among its
wikilinks, so both are on the table.

## The experiments

Because links are text, their whole
behaviour can be audited without the
app — and was. The lab's checker
(`obsidian-lab/scripts/check_vault.py`)
applies exactly the two rules above
to the vault's files and reports what
resolves. Baseline
(`obsidian-lab/transcripts/t01-links-baseline.txt`):
**9 notes, 26 links, all resolve.**

Then the lab did to copies of the
vault the two things users do to
files without thinking:

**Rename.** `Tomatoes.md` was
renamed, by hand in the file system,
to `Tomato Varieties.md`
(`obsidian-lab/transcripts/t03-rename-breaks.txt`).
Six links broke: every `[[Tomatoes]]`
(five of them, across five notes) now
names a note that is not there, and
the Markdown link `(Tomatoes.md)` in
the seed inventory paths to a file
that is not there either. Renaming a
file renames nothing inside the other
files. The words still say what they
said.

**Move.** `Compost.md` was moved, by
hand, into a new folder, `Beds/`
(`obsidian-lab/transcripts/t04-move-survival.txt`).
Exactly **one** link broke: the
Markdown link in `Home.md`, which
points at the path `Compost.md` and
the file is no longer at that path.
Every `[[Compost]]` wikilink still
resolves, because a name does not
care which shelf the note sits on.

That asymmetry is the chapter in one
paragraph: **wikilinks survive moves
and break on renames; path links
break on both** — unless the renaming
and moving happen *inside* Obsidian,
where the app sees the act and
rewrites the links across the vault
as part of it. (That rewriting has
its own setting and its own limits:
it fixes the links it knows about,
in the vault it can see.) Work on
your vault's structure from inside
the app, or audit afterwards with a
checker like the lab's — those are
the two safe ways, and mixing them
unthinkingly is how vaults quietly
rot.

## Which style should you use

Honest answer: either, held to
consistently, beats both held loosely.

- **Wikilinks** if the vault lives
  its life in Obsidian and its
  cousins: shorter to type, kinder to
  reorganising, and the display alias
  is graceful. Their cost is paid
  outside the family — other Markdown
  tools show `[[Compost]]` as plain
  text with brackets, a link to
  nowhere.
- **Markdown links** if the notes
  must read correctly everywhere —
  published, rendered by other tools,
  or kept for a future that may not
  include this app. Their cost is the
  path discipline: folders become
  load-bearing.
- The lab's gardener, being
  fictional and methodical, uses
  wikilinks inside the notebook and
  would switch for anything leaving
  it. Your rule can differ; having a
  rule cannot.

Check: in the lab vault, count the
links to `Tomatoes` with the checker
or by eye — six. The real app, given
the same vault, reported **6
backlinks** (`obsidian-lab/transcripts/t07-appimage-run.txt`).
When two independent readers of the
same files agree on the bookkeeping,
the bookkeeping is the files. That
is the deepest fact in this guide,
and chapter 6 spends it.
