#!/usr/bin/env python3
"""Install this chat archive into Claude Code on your Mac.

Afterwards the chats show up in your Claude Code sidebar, pinned, under their
original names — open any one and the whole conversation is there, ready to
continue. Nothing you already have is deleted.

    python3 install.py                    # installs into ~/Desktop/Jarvis
    python3 install.py ~/code/jarvis      # or wherever you keep the vault

Quit Claude Code first (Cmd+Q). Relaunch when it finishes.
"""
import json, os, shutil, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.expanduser("~/Library/Application Support/Claude")
VAULT = os.path.abspath(os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/Desktop/Jarvis"))


def die(msg):
    print("\n  " + msg + "\n")
    sys.exit(1)


if not os.path.isdir(APP):
    die("Claude Code desktop isn't installed on this Mac (no ~/Library/Application Support/Claude).")
if not os.path.isdir(VAULT):
    die(f"No vault at {VAULT}.\n  Clone it first, or pass the right path: python3 install.py /path/to/vault")

manifest = json.load(open(os.path.join(HERE, "manifest.json")))
print(f"\n  Installing {len(manifest)} chats")
print(f"  vault: {VAULT}")

# ---------------------------------------------------------------- transcripts
# Claude Code finds a session's transcript by the working directory it ran in,
# encoded with slashes turned into dashes.
slug = "-" + VAULT.strip("/").replace("/", "-")
proj = os.path.expanduser(f"~/.claude/projects/{slug}")
os.makedirs(proj, exist_ok=True)
copied = 0
for m in manifest:
    src = os.path.join(HERE, "raw", m["cliSessionId"] + ".jsonl")
    if not os.path.exists(src):
        print(f"  ! missing transcript for {m['title']}")
        continue
    shutil.copy2(src, os.path.join(proj, m["cliSessionId"] + ".jsonl"))
    copied += 1
print(f"  transcripts: {copied} -> {proj}")

# ------------------------------------------------------------------- sidebar
# Each chat in the sidebar is one small json file under the signed-in account's
# folder. We write one per session, pointing at the transcript above.
try:
    account = json.load(open(APP + "/config.json"))["lastKnownAccountUuid"]
except Exception:
    die("Couldn't tell which account you're signed into. Open Claude Code once, sign in, quit, and re-run.")

acct_dir = os.path.join(APP, "claude-code-sessions", account)
slices = [d for d in sorted(os.listdir(acct_dir)) if os.path.isdir(os.path.join(acct_dir, d))] \
    if os.path.isdir(acct_dir) else []
if not slices:
    die(f"No session folder for your account yet.\n  Open Claude Code, start any chat, quit, then re-run this.")
target = os.path.join(acct_dir, slices[0])

now = int(time.time() * 1000)
local_ids = []
for m in manifest:
    cli = m["cliSessionId"]
    sid = "local_" + cli
    local_ids.append(sid)
    json.dump({
        "sessionId": sid,
        "cliSessionId": cli,
        "cwd": VAULT,
        "originCwd": VAULT,
        "createdAt": m.get("createdAt") or now,
        "lastActivityAt": m.get("lastActivityAt") or now,
        "lastFocusedAt": m.get("lastActivityAt") or now,
        "model": "claude-opus-5",
        "isArchived": False,
        "title": m["title"],
        "titleSource": "user",
        "permissionMode": "default",
    }, open(os.path.join(target, sid + ".json"), "w"), indent=1)
print(f"  sidebar entries: {len(local_ids)} -> account {account[:8]}")

# ---------------------------------------------------------------------- pins
cfg_path = APP + "/claude_desktop_config.json"
backup = cfg_path + f".backup-{now}"
shutil.copy2(cfg_path, backup)
cfg = json.load(open(cfg_path))
prefs = cfg.setdefault("preferences", {}).setdefault("epitaxyPrefs", {})
slice_prefs = prefs.setdefault("dframe-local-slice", {})

order = slice_prefs.setdefault("pinnedOrder", [])
for sid in reversed(local_ids):                       # newest ends up on top
    tag = "code:" + sid
    if tag not in order:
        order.insert(0, tag)

starred = prefs.setdefault("starred-local-code-sessions", [])
for sid in local_ids:
    if sid not in starred:
        starred.append(sid)

json.dump(cfg, open(cfg_path, "w"), indent=1)
print(f"  pinned: {len(local_ids)} (config backed up to {os.path.basename(backup)})")

print(f"""
  Done. Relaunch Claude Code.

  The chats are in your sidebar under their original names. Open one and read
  it, or just keep typing — it carries on with everything already in context.

  Heads up: file paths inside old messages point at Ansh's machine, so if a
  chat re-reads a local file it may come up empty. The conversation itself
  replays fine.
""")
