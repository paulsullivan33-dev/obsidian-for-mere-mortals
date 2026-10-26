# The Vault

Outcome: you can look at a vault on
disk and name every part of it — what
is a note, what is an attachment, and
what is the app's own settings — and
you know the one safe experiment:
delete the settings, keep the notes.

## A folder, nothing more

A **vault** is a folder. Create one
and Obsidian offers to keep its notes
there; point Obsidian at a folder
that already holds Markdown files, as
the lab did, and it adopts them as
they lie. Notes can sit in subfolders
— the lab's daily notes live in
`Daily Notes/`, its templates in
`Templates/` — and the folder's name
becomes the vault's name in the app.

The lab's vault, complete, is nine
notes and a picture
(`obsidian-lab/transcripts/t00-vault-tree.txt`):

```text
vault/Home.md
vault/Tomatoes.md
vault/Compost.md
vault/Seed Inventory.md
vault/Watering Schedule.md
vault/Garden Map.md
vault/Daily Notes/2026-04-02.md
vault/Daily Notes/2026-04-03.md
vault/Templates/Crop Record.md
vault/Attachments/garden-plan.png
```

Every one of those is an ordinary
file. `Tomatoes.md` is 518 bytes of
text you can read with any tool made
since the 1970s, and chapter 5's
checks read it with exactly such
tools.

## The hidden room: .obsidian

Inside the vault sits one folder that
is not yours: **`.obsidian`**, hidden
on most systems because its name
begins with a dot. It is where the
app keeps what it needs to remember
about *this* vault:

- **`app.json`** — settings for this
  vault (how links are written, where
  attachments go, and the like).
- **`appearance.json`** — theme and
  fonts, for this vault.
- **`core-plugins.json`** — which of
  the built-in features are switched
  on here (chapter 12 reads the real
  one).
- **`workspace.json`** — the layout:
  which panes were open, on which
  note, when the app last closed.
  This is per-machine state wearing a
  vault's clothes, and chapter 11
  explains why syncing it between two
  computers is the one file worth
  arguing about.
- More files appear as features are
  used: the lab's app wrote
  `graph.json` (the graph view's
  settings) only after the graph was
  first opened.

Two facts make `.obsidian` safe to
understand and safe to mistrust
appropriately. First, it is all
**JSON** — plain text in a standard
shape. The lab parsed every file in
it with a thirty-year-old idea and a
short script
(`obsidian-lab/transcripts/t06-properties-and-config.txt`),
and nothing in it is your prose.
Second, it is disposable: delete the
whole folder and Obsidian rebuilds it
with defaults the next time it opens
the vault. Your notes are untouched,
because they were never in there.

That is also the diagnostic this
chapter promised: a vault that
behaves oddly — wrong theme, strange
settings, a plugin list you do not
recognise — can be reset by closing
the app and renaming `.obsidian`
aside. If the oddity vanishes, it was
a setting. If it survives, it is in
your files, and chapter 18 takes it
from there.

## What is not in the vault

Two things readers often go looking
for inside the folder are kept
elsewhere:

- **The app's list of your vaults**
  lives in your user profile, in the
  app's own configuration (`obsidian.json`
  under its config folder). That is
  how the launcher on a new start
  knows which vaults to offer — and
  why copying a vault folder to a new
  machine does not make the new
  machine's Obsidian know it exists
  until you open it once (chapter 3).
- **File recovery snapshots** — the
  app's short-term safety net for
  edits (chapter 12) — are also kept
  per user, not per vault. They are a
  convenience, not a backup, and
  chapter 17 is blunt about the
  difference.

## One vault or several

A vault is a boundary the app
respects: links, search, the graph
and plugins all stop at its walls.
Two vaults cannot link to each other.
So the practical rule: one vault per
world that should not leak into
another — the work notebook and the
private diary are separate vaults for
the same reason they are separate
diaries — and one vault per world,
not per topic. Topics are what
folders, links and tags are for, and
they cost nothing; vaults cost a
wall.

Check: open the lab vault's folder in
your ordinary file manager. Hide
nothing. Every file you see is either
a note you could read aloud, the
picture from chapter 10, or a
settings file from this chapter. If
you can say which is which at a
glance, the vault holds no more
mysteries.
