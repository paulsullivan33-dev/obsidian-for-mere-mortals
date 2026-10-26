# Dataview, Publish and Bases

Outcome: you know what the three most
asked-about extras do, which of them
are the maker's and which are not,
and what each costs — in money, in
discipline, or in trust. This chapter
is an outline from the documentation,
and says so on its face: the lab ran
none of the three, and pretends
otherwise nowhere.

## Dataview: asking questions of the vault

**Dataview** is the best-known
community plugin (chapter 13's rules
apply to it in full — it is famous,
kept, and still somebody else's
program). It treats your notes as a
small database and answers queries
written in a query language of its
own, inside the note that asks:

```text
TABLE status, sown
FROM #crop
WHERE status = "growing"
```

— a live table of every growing crop,
rebuilt each time the note opens,
from the properties of chapter 7 and
the tags beside them. It is the
payoff the properties chapter
promised: facts kept as data can be
*gathered*, not just read one note
at a time.

What the outline must add, honestly:
the query language is a real language,
with a learning curve measured in
evenings; the tables live only where
Dataview runs, so the note outside
the app shows the question, not the
answer; and a vault wired deeply
into Dataview has quietly chosen its
tool for the long term. For many
notebooks that is a trade made
gladly and with open eyes. Make it
with open eyes.

## Bases: the maker's answer, arriving

**Bases** is the maker's own version
of the same idea, and it is a *core*
plugin in current versions — its
presence in the lab's own vault is
one of the few things in this chapter
the lab did verify: `bases` sits in
the app's `core-plugins.json`, and
the new-tab page offered a "New
base" button unprompted
(`obsidian-lab/transcripts/t06-properties-and-config.txt`,
t07). A **base** is a view over the
vault's files — a table, to start
with — filtered and sorted by
properties, saved as a `.base` file
in the vault, itself a plain YAML
document you can read.

The difference from Dataview, in one
breath: Bases is narrower, younger,
and the maker's — no community
plugin to trust, an open file format
of its own, and a feature set still
growing into the job. If your need
is "a table of my crops by status",
Bases is now the first door to try;
if your need is a query language
with a decade of community answers
behind it, Dataview is the famous
one. The guide takes no side beyond
that ordering, and neither should a
first month with the app.

## Publish: the vault, on a website

**Publish** is the maker's paid
service for turning selected notes
into a website on their hosting,
under your name: choose the notes,
press publish, and the links, graph
and search travel with them in a
reader-friendly skin. It is a core
plugin's switch (`publish`, off by
default in the lab's census) with a
subscription behind it.

Its honest outline needs three
sentences. It is by far the easiest
way to put a notebook on the web —
easier than this guide's own MkDocs
machinery. What you publish is a
*copy*, and copies are chapter 1
decisions: a private note one folder
away from a public one deserves the
same care as the sync choice in
chapter 11. And the site lives at
the service's pleasure and pricing;
the vault, as ever, remains yours
either way.

Check: you can place each of the
three in one clause — *Dataview, a
stranger's query engine, powerful
and trusted by many; Bases, the
maker's young built-in, narrower and
native; Publish, the maker's paid
door to the web.* Chapters get
written when a guide can run a thing.
This one could not, and the outline
is labelled accordingly — which is
itself the last lesson of the trio.
