# Installing Obsidian

Outcome: Obsidian is installed, you
have met its launcher, and you have
opened a folder as a vault — the
lab's way first, then your own.

## Getting the app

Obsidian is a desktop program for
Windows, macOS and Linux, with phone
and tablet companions discussed below.
Downloads come from one place only:
**obsidian.md**. Installers appear
elsewhere on the internet, some of
them bundled with things you did not
ask for; the rule from chapter 1
applies to software about your diary
with double force. Download from the
maker, or do not download.

- **Windows and macOS:** an ordinary
  installer; run it, and Obsidian
  appears in your programs like
  anything else.
- **Linux:** the project ships an
  **AppImage** (one file that is the
  whole app), a `.deb` for
  Debian-family systems, a `.tar.gz`,
  and packages through community
  channels such as Flatpak and Snap.
  The AppImage is the maker's own and
  the one this guide's lab used:
  download it, mark it executable,
  run it.
- **Phones and tablets:** the Apple
  App Store and Google Play carry the
  mobile apps. They read the same
  vaults, with the differences chapter
  17 lists; getting a vault onto the
  phone is a sync question, and it
  belongs to chapter 11.

The lab's install, for the record
(`obsidian-lab/transcripts/t07-appimage-run.txt`):
the official AppImage for **Obsidian
1.14.5**, 139 MB, extracted and run on
a virtual screen in the sandbox. No
account was created at any point —
none is asked for.

## The launcher

First launch shows the **launcher**:
the app's name, its version, and
three doors.

- **Create new vault** — make a fresh
  folder, empty but for a `.obsidian`,
  and start writing in it.
- **Open folder as vault** — point at
  a folder of Markdown files that
  already exists. Obsidian adopts it
  as it lies; this is the door the lab
  used, and the door for any folder of
  notes you already keep.
- **Open vault from Obsidian Sync** —
  the paid door; chapter 11 covers it
  as documentation, since the lab
  signed in to nothing.

Underneath sits a language choice,
and that is the whole screen. There
is no account wall, no trial clock,
no tour to dismiss. For an app whose
entire pitch is *your files, your
machine*, the first screen is the
pitch kept.

## Opening the lab vault

Try the lab's vault before your own;
it is safe to break, and later
chapters break it on purpose. Copy
`obsidian-lab/vault/` from this
guide's repository to somewhere
ordinary — your documents folder will
do — launch Obsidian, choose **Open
folder as vault**, and select the
copy. The app thinks for a moment,
writes a `.obsidian` folder into the
copy if it lacks one (the guide's
copy already carries the one the
lab's app wrote), and shows the
explorer down the left side: nine
notes in their folders.

That explorer is the folder, drawn
tidily. Nothing was imported, because
there was nothing to import *from* —
the files were already the notes.
Click `Home` and you are reading the
gardener's front door, links and all;
the status bar at the bottom already
knows it has **2 backlinks**, a claim
chapter 6 will make you able to
audit by hand.

## Your own first vault

When you make your own, decide two
things and leave everything else at
defaults:

- **Where it lives.** A folder you
  control, inside whatever backup
  habit you already keep. Not inside
  another vault — vaults do not nest
  happily.
- **What it is for.** One world, per
  chapter 2: the diary, the project,
  the study notes. The name of the
  folder is the name of the vault;
  call it what the world is called.

Then write one note — tomorrow's
chapter is that note, taken
seriously.

Check: close the app and open your
file manager. In the vault you just
opened there is a `.obsidian` folder
that was not there before, and your
notes are exactly as you left them.
The app has moved into the folder
without rearranging the furniture —
which is the whole idea, and the
subject of the next chapter.
