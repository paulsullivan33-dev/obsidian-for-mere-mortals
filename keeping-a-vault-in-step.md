# Keeping a Vault in Step

Outcome: your vault exists on the
machines and the phone where you
need it, you chose the copying method
with your eyes open about who else
holds a copy, and a **sync conflict**
is an annoyance you recognise, not a
loss you discover.

## The choice underneath the choices

A vault is a folder, so *any* tool
that copies folders can keep it in
step: that is the freedom chapter 1
promised, and it comes with a duty
the other apps spared you. Somebody's
servers will hold a copy of your
diary, or nobody's will, and which of
those is true is decided here, by
the method you pick. Read the three
honest options with that sentence in
mind. The lab, having nothing to
sync and no account, ran none of
them; this chapter is documentation
and arithmetic, and says so.

## Option one: Obsidian Sync

The maker's own service. It is a
**core plugin** — listed in the
`.obsidian/core-plugins.json` the
lab's app wrote — switched on with a
paid subscription and a sign-in.

- **For it:** built for exactly this
  folder; syncs notes, attachments
  and (as much of) the settings as
  you allow, per device; version
  history kept on the service;
  selective sync for big files.
- **Its privacy shape:** copies are
  **end-to-end encrypted** — the
  service holds ciphertext it cannot
  read, with your password the key.
  Of the three options, this is the
  only one whose operator *cannot*
  read your notes even in principle.
- **Against it:** it costs money,
  forever, and the vault's
  portability now includes a habit of
  paying. The encryption protects
  content, not metadata, and the
  service is still one company's —
  the exit, as ever, is that the
  folder remains yours throughout.

## Option two: git

Treat the vault as a code repository
and sync it the way programmers sync
text: commits, pushes, a remote.
Community plugins automate the
button-pressing (chapter 13's rules
apply to them in full).

- **For it:** a real history of every
  change, on infrastructure you may
  already trust; superb for text;
  free at small scale; the diffs of a
  diary are a strange and wonderful
  read.
- **Its privacy shape:** the remote
  holds the vault **readable** by
  whoever runs it, unless you host it
  yourself. A public repository is a
  published diary; check the setting
  twice, then a third time.
- **Against it:** attachments are
  ballast git carries badly; two
  machines editing offline produce
  merge conflicts in prose, which are
  exactly as fun as they sound; and
  phones make git an expedition
  rather than a habit.

## Option three: a file-sync tool

Point a general syncing program —
the kind that keeps any folder in
step between machines — at the
vault, and let it do its ordinary
job. (This series' *Syncthing for
Mere Mortals* teaches one such tool
whole; the argument here needs only
the shape.)

- **For it:** no account with the
  notes' maker, works for every
  folder you own, and some such tools
  sync machine to machine with no
  server of anyone's in between.
- **Its privacy shape:** entirely
  the tool's. A server-based tool
  holds a readable copy unless it
  encrypts; a machine-to-machine one
  holds none. Read its shape, not its
  slogan.
- **Against it:** it knows nothing
  about notes. It copies
  `.obsidian/workspace.json` — chapter
  2's per-machine layout — back and
  forth, so two computers can spend
  their days swapping window layouts;
  most users exclude that one file.
  And its conflicts are file-level:
  two edits to one note on two
  machines arrive as a *conflicted
  copy* beside the original, to be
  reconciled by hand. The note is not
  lost. It is, however, now homework.

## The conflict, met calmly

Every method meets the same day: the
note edited on the train and at the
desk before either saw the other.
Sync services merge or version;
file-sync tools duplicate; git
objects. None loses the words if you
understand which of the three yours
does — and the understanding is the
deliverable of this chapter.
Whatever you chose: check in a week
that the copies agree, and check
after the first conflict that they
still do. Trust in a sync is a thing
you verify early, while the stakes
are a tomato note.

Check: your chosen method, named,
and one sentence: *who else can read
the copy, and what happens on a
conflict.* If the sentence is
comfortable, the vault is in step.
If it is not, the folder is still
yours — changing your mind costs a
setting, not your notes. That was
the point of chapter 1, and this
chapter is where it pays out.
