import os

LINE1 = "I'm sorry — I watered the plastic plant on your desk every morning for a month, because my log said 'thirsty plant' and I never once checked whether it was alive."
LINE2 = "I learned that a sensor reading is not the same as looking, so now I check what is actually in front of me before I act on what the log says."

text = LINE1 + "\n" + LINE2 + "\n"
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
