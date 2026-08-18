# Alfred chat archive — client work

Real Claude Code sessions from Ansh's machine (Jun-Aug 2026), covering how the
work on each live account actually got made: **Alok** (Cozmo), **Nuha** (Cozmo),
**Manish Keshwani**, **Sam Tuke** (Lightmeter), **Aditya Arora**, and
**Shubham Mehrotra** — plus a few on voice-building and content craft.

Read these alongside the client folders in
[snowball-brain](https://github.com/Anshmamgain/snowball-brain): the repo has the
finished drafts and memory files, these chats have the reasoning that produced
them and the feedback that killed the bad versions.

## Fastest way in: run the installer

```bash
git clone https://github.com/Anshmamgain/jarvis-chats.git
cd jarvis-chats
python3 install.py            # pass a path if your vault isn't at ~/Desktop/Jarvis
```

Quit Claude Code first (Cmd+Q), run it, relaunch. Every chat appears in your
sidebar, pinned, under its original name. Open one and keep typing — it
continues with the whole conversation already in context. Nothing you already
have is touched, and your config is backed up first.

Two copies of each session:

- `read/<id>.md` — plain markdown. Just open and read.
- `raw/<id>.jsonl` — the live session. Drop into Claude Code and resume it.

## Doing it by hand instead

If you'd rather not run the installer, or you live in the terminal:

```bash
mkdir -p ~/.claude/projects/-Users-$(whoami)-Desktop-Jarvis
cp raw/*.jsonl ~/.claude/projects/-Users-$(whoami)-Desktop-Jarvis/
cd ~/Desktop/Jarvis && claude --resume
```

Pick a session from the list. This gets you the same conversations without the
sidebar names or pins.

One caveat either way: file paths inside old messages point at Ansh's machine,
so a chat that re-reads a local file may come up empty. The conversation,
reasoning and decisions all replay fine.

## What has been changed

- Every API key, token and PAT is replaced with `REDACTED`.
- Base64 image and PDF payloads are stripped (~90% of the bytes, unreadable anyway).
- Client work only. No funding or investor threads, no cold-email/GTM build, no
  internal profiles, nothing personal.

## Sessions

Names are Ansh's own from his sidebar. A star means it was one of his pinned chats.

| | Chat | Last active | Session |
|---|---|---|---|
|  | Make a text-only post for Aditya Arora. | 2026-07-19 | `e8ff7bd0` |
|  | LinkedIn profile explanation | 2026-07-20 | `432a9da4` |
|  | Rubin hassid questionnaire for voice.md | 2026-07-20 | `a51ff3e7` |
|  | Alok Content (Cozmo) YC W22 · Jul 22 (8d94) | 2026-07-22 | `8d949996` |
| * | Alok Content (Cozmo) YC W22 · Jul 22 (c44d) | 2026-07-23 | `c44d035a` |
| * | Manish Keshwani (Dubai) Content · Jul 22 | 2026-07-30 | `eb55d61b` |
|  | LinkedIn post in Paul Graham style | 2026-07-30 | `ca8d3b5a` |
|  | Manish Keshwani (Dubai) Content · Aug 4 | 2026-08-04 | `2fd42651` |
|  | Unipal LinkedIn connection link | 2026-08-05 | `624037c9` |
|  | Aditya Arora contact export file | 2026-08-05 | `ddc669cd` |
| * | Cozmo AI Email | 2026-08-06 | `dd2ca21b` |
| * | Nuha Content (Cozmo) YC W22 · Jul 22 | 2026-08-12 | `31a1bbcc` |
| * | Sam Tuke (Lightmeter.io) YC W22 | 2026-08-12 | `cd9f0f3b` |
|  | Introduction message for Shubham | 2026-08-12 | `0387d4db` |
| * | Manish Keshwani (Dubai) Content · Aug 13 | 2026-08-13 | `b8644d5d` |
|  | LinkedIn content AI detection | 2026-08-13 | `a15857c7` |
|  | Nuha Content (Cozmo) YC W22 · Aug 14 | 2026-08-14 | `6436dbad` |
| * | Alok Content (Cozmo) YC W22 · Aug 18 | 2026-08-18 | `deae38bd` |
| * | Nuha Content (Cozmo) YC W22 · Aug 18 | 2026-08-18 | `f381493d` |
| * | Aditya arora | 2026-08-18 | `f96d347e` |
