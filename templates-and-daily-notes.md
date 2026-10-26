# Templates and Daily Notes

Outcome: you can stamp out a new note
with its shape — headings, properties,
standing links — already in place, and
keep a note a day without thinking
about names or folders at all.

## Templates: the shape, filled in

A **template** is a note kept in a
folder the app is told about (the lab
keeps its in `Templates/`), whose text
is copied into new notes on request by
the **templates** core plugin. Inside
the template, a few **variables** in
double braces are filled in at the
moment of copying:

- `{{date}}` and `{{time}}` — today,
  in the format you choose.
- `{{title}}` — the new note's name.

The lab's crop record is the whole
idea in fifteen lines:

```markdown
---
type: crop
status: planned
sown:
bed:
---

# {{title}}

Sown on {{date}}.

Fed from the [[Compost]] heap,
watered by the [[Watering Schedule]].
```

Make a note from it and three kinds of
work are already done: the properties
of chapter 7 exist (empty, waiting,
but *spelt right*), the standing links
of chapter 5 are present, and the
headings are the ones every crop note
shares. Templates are how a vault's
discipline survives its author's busy
weeks — not by willpower, but because
the correct shape is the path of
least resistance. A template folder
holds a handful at most: one per kind
of note you make weekly. A template
for every mood is a bureaucracy, and
chapter 17 keeps an eye on those.

## Daily notes: a note a day

The **daily notes** core plugin does
one small thing perfectly: it keeps a
note per day, in a folder you name
(the lab's is `Daily Notes/`), named
by a date format you choose
(`2026-04-02` in the lab), created
from a template you point at, and
opened by one click or shortcut —
today's, or the day you are looking
at from the calendar of your week.
The lab's two daily notes show the
genre: short, dated by their
existence, and liberal with links —
`[[Tomatoes]]` planted out today —
because chapter 6's backlinks will
gather those scattered days under
each subject's note for free.

Daily notes are where a vault earns
the word *notebook*. Everything else
in this guide is structure; this is
the habit the structure serves. Two
settings deserve a thought on day
one: the **date format** (pick the
sortable `YYYY-MM-DD` and never
revisit it — names that sort are
names the file system, the switcher
and any future tool all agree on),
and the **template**, which can be
as small as a heading and three
prompts you actually answer.

Check: read the lab's template and
then the lab's tomato note side by
side. Same properties, same links,
same skeleton — the template is the
note with the facts left blank. If
your own templates do not produce
that family resemblance at a glance,
they are essays, not templates.
