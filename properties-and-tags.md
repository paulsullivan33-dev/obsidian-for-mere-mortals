# Properties and Tags

Outcome: you can give a note facts
about itself — its type, its status,
the day it was sown — in a form the
app reads as data, and sprinkle tags
through your writing knowing exactly
what a tag is and is not.

## Properties: facts at the top of the note

A note can open with a block of
**properties**: name-and-value pairs
in **YAML**, the plain-text data
format, fenced by two lines of three
dashes. The lab's tomato note begins:

```yaml
---
type: crop
status: growing
sown: 2026-03-14
bed: north
---
```

That block is called **front matter**
in the wider Markdown world. In the
file it is six lines of text. In the
app it becomes the **properties
panel** you saw in chapter 3: a tidy
form at the top of the note where
each property can be edited as a
field, not as text. The lab proved
the two views are one thing both
ways — a plain YAML parser read the
same block and reported the same
facts, including a subtle one: the
`sown` value came back as a real
*date*, not a string of digits
(`obsidian-lab/transcripts/t06-properties-and-config.txt`).
The app noticed too: it drew a
calendar icon beside that field.

Property **types** keep the data
honest. A property can be text, a
list, a number, a checkbox, a date,
or a date-and-time, and the app holds
every note's use of that property to
the type you set for it. Three
property names are reserved by the
app itself: **`tags`** (the note's
tags, next section), **`aliases`**
(other names this note answers to —
which wikilinks then accept), and
**`cssclasses`** (styling hooks,
which this guide leaves alone).

Why bother? Because properties are
the difference between notes you
*read* and notes you can *ask
questions of*. "Which crops are still
growing?" is a question about a
property; it cannot be asked of
prose. Chapter 14 builds on exactly
that. The discipline is the cost:
a property only answers if every
relevant note carries it, spelt the
same way, every time. Templates
(chapter 9) are how the discipline
stays cheap.

## Tags: labels in the margin

A **tag** is a word with a `#` in
front of it — `#crop`, `#summer` —
typed anywhere in a note's text, or
listed in its `tags` property. Tags
are looser than properties on
purpose: no types, no values, just
labels. Clicking one finds every
note carrying it; the **tag pane**
lists the vault's tags with counts.
Tags can **nest** with a slash —
`#crop/summer` files summer under
crop — which gives a light hierarchy
without any machinery.

Being plain text, tags are findable
without the app; the lab found the
gardener's with an ordinary text
search (`obsidian-lab/transcripts/t05-tags-and-text.txt`).
That cuts both ways, and the cut is
worth knowing: a `#crop` in a
sentence is a tag, and so is any
other `#word` you type — the app
cannot tell your label from your
emphasis. Tags are a habit, not a
filing system imposed from above.

## Properties or tags: which, when

A working rule that survives contact
with real notebooks:

- **Tags** for moods, seasons, and
  cross-cutting labels you apply in
  passing — things a note *is like*.
  Cheap to add, forgiving of mess.
- **Properties** for facts you will
  later sort, filter, or count —
  things a note *has*: a status, a
  date, a place, a type. Worth the
  small ceremony of the front matter.
- Neither, most days. A note whose
  only structure is clear prose and
  good links is not unfinished. The
  machinery of this chapter serves
  the writing; the day it starts
  being served *by* the writing,
  chapter 17 has a paragraph for you.

Check: open the lab's `Seed
Inventory.md` in a text editor. Its
front matter says `type: inventory`,
an `updated` date, and a `place` —
and the chapter's parser transcript
(t06) reads all three without the
app. If you can read a note's facts
with the app closed, you own the
facts; the app is only lending you
its spectacles.
