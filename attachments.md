# Attachments

Outcome: you can put a picture — or a
PDF, a sound file, a spreadsheet —
into a note, know exactly where the
file landed, and move it later
without orphaning it.

## An attachment is just a file that is not a note

Notes are Markdown. Everything else a
vault holds — the photograph of the
bed, the scanned seed catalogue, the
recording of the meeting — is an
**attachment**, and it lives in the
vault as an ordinary file, exactly as
boring as that sounds. The lab's one
attachment is `Attachments/garden-plan.png`,
746 bytes, and its transcript
(`obsidian-lab/transcripts/t05-tags-and-text.txt`)
shows it being found by the plainest
tools on the machine.

A note displays an attachment with an
**embed** — a link with an
exclamation mark in front, in either
of chapter 5's styles:

```markdown
![[garden-plan.png]]
![The garden plan](Attachments/garden-plan.png)
```

The wikilink form finds the file by
name, vault-wide; the Markdown form
points by path, with the usual
consequences from chapter 5 when
things move. The lab's map note uses
the wikilink form, and its checker
verifies the embed exactly as it
verifies any other link.

## Where new attachments land

When you paste or drag a file into a
note, the app must put it *somewhere*,
and the setting (in `app.json`, under
Files & Links behaviour) offers three
answers: the vault's root, a **named
attachment folder** — the lab's
`Attachments/` is the tidy choice —
or a subfolder beside the note that
uses it. Choose the named folder.
Root-level scatter is how vaults get
their reputation for mess, and
beside-the-note scatters the same
files more privately but no more
findably. One folder, named for its
job, is the whole system.

Two honest notes on attachments:

- **They are not compressed, indexed
  or transcribed.** A photograph sits
  in the vault at the size it arrived.
  A vault is a fine home for the
  picture a note discusses and a poor
  one for ten thousand raw camera
  files — chapter 11's sync arithmetic
  will make that concrete.
- **Renaming obeys chapter 5.**
  Rename an attachment inside the app
  and the embeds are rewritten;
  rename it in the file system and
  every `![[old name]]` dangles until
  fixed. The lab's checker counts
  embeds among its links, so its
  verdicts cover pictures too.

Check: the embed in `Garden Map.md`
says `![[garden-plan.png]]`. The file
is in `Attachments/`. Nothing in that
sentence required the app — which is
how you know the note will still
show its picture, or honestly report
its absence, in whatever tool reads
it next.
