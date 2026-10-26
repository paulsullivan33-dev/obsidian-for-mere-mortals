# Troubleshooting

Outcome: the six failures a new vault
meets first, each with the cause the
lab or the file model makes provable,
and the fix in the order to try it.

## The link is red and goes nowhere

**Symptom:** a `[[wikilink]]` shows
as unresolved and clicking it offers
to create a new note.

**Causes, in order.** The target note
was renamed *outside* the app, so
the words in your note still name
the old name — the lab's transcript
t03 is this failure manufactured on
purpose, six times over. Or the name
is simply misspelt, yours or the
file's. Or the note lives outside
the vault's walls, where links cannot
reach.

**Fix.** Read the file names, not
your memory of them. Rename inside
the app from now on so links are
rewritten as part of the act
(chapter 5), and audit a vault you
have rearranged by hand with a
checker like the lab's before
trusting its link counts again.

## The picture is missing from the note

**Symptom:** an embed shows a broken
frame where the photograph was.

**Causes.** The attachment was moved
or renamed outside the app (chapter
10's rule, broken), or the note came
from elsewhere and its attachments
did not travel with it, or the embed
uses a path and the note moved
folders, changing what the path
means.

**Fix.** Find the file first — search
the vault folder for its name with
the file manager, not the app. If it
is there under a new name, fix the
embed or rename the file back,
inside the app. If it is not there,
the note was never the picture's
keeper: restore the file from the
copy of the vault chapter 11 made
you keep, into the attachment
folder, under its old name.

## The properties panel is not showing

**Symptom:** a note with front matter
shows raw dashes and text at the top,
or no panel where the panel should be.

**Causes.** The **properties** core
plugin is off in this vault
(chapter 12's census is the check).
Or the front matter is malformed:
YAML is fussy about colons inside
unquoted values and about indentation,
and one bad line retires the whole
block to plain text. Or the block is
not at the very first line of the
file, where alone it counts as front
matter.

**Fix.** Check the switch; then check
the block — quoting a value that
contains a colon (`place: "shed: the
back one"`) cures the commonest case.
The lab's parser (transcript t06)
reads front matter with a standard
YAML library: if it is happy and the
app is not, the difference is worth
a screenshot and a slow comparison.

## The vault opens empty

**Symptom:** the app shows a vault
with no notes, under the right name
or a wrong one.

**Causes.** You opened the folder
*above* the vault, or a copy of it —
the vault is the folder that directly
holds the notes and its `.obsidian`.
Or a sync tool is still delivering
the files, and the vault is honestly
empty *so far*.

**Fix.** Close the vault. In the file
manager, walk to the folder where the
`.md` files actually are; open *that*
folder as the vault. The lab's tree
(transcript t00) is the shape to
expect: notes and `.obsidian` in the
same room, not in neighbouring ones.

## Two versions of a note appeared

**Symptom:** `Tomatoes.md` has a
sibling with "conflicted copy" or a
date in its name, and the two differ.

**Causes.** Chapter 11's day arrived:
the note was edited in two places
before they synced. Your method has
done its honest best; the rest is
yours.

**Fix.** Open both, merge by hand —
the differences are sentences, not
binary — keep the merged note under
the original name so its links (and
backlinks) survive, and delete the
conflicted sibling inside the app.
Then ask the chapter 11 question
while it is cheap: is this method's
conflict behaviour the one you
chose, or the one you drifted into?

## The app forgot the vault exists

**Symptom:** the launcher offers to
create or open, and your vault is not
listed.

**Causes.** The vault list lives in
the app's configuration in your user
profile (chapter 2) — a new machine,
a new profile, or a cleaned profile
forgets the *list*, never the vault.

**Fix.** **Open folder as vault**,
point at the folder, carry on. The
notes were never in the list; they
were in the folder, which was the
point of the design and of this
book.

Check for the whole chapter: every
fix began in the file manager or in
`.obsidian`, not in a reinstallation.
A tool whose failures are inspectable
in its own folder is a tool whose
failures stay small.
