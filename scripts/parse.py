comments_file = "data/comments.txt"

with open(comments_file, "r", encoding="utf-8") as f:
    comments = f.readlines()

# skip first 25 lines
comments = comments[25:]
# skip last 8 lines
comments = comments[:-8]

# skipping view all replies and likes
comments_1 = []
for line in comments:
    if line.startswith("View all ") or line.endswith("like\n") or line.endswith("likes\n"):
        # print("Skipping comment:", line)
        continue
    comments_1.append(line)

# skipping Reply button
skipcount = 0
comments_2 = []
for line in comments_1:
    if skipcount > 0:
        skipcount -= 1
        # print("Skipping comment:", line)
        continue
    else:
        if line.startswith("Reply\n"):
            skipcount = 4
            # print("Skipping comment:", line)
            continue
        else:
            comments_2.append(line)

# join 3 lines into 1
comments_3 = []
for i in range(0, len(comments_2), 3):
    comments_3.append(comments_2[i] + comments_2[i + 1] + comments_2[i + 2])

comments_4 = []
for comment in comments_3:
    # replace newline characters with | character
    comment = comment.replace("\n", "|")
    comments_4.append(comment)

# write comments to file
comments_file = "data/comments_cleaned.txt"
with open(comments_file, "w", encoding="utf-8") as f:
    for comment in comments_4:
        f.write(comment + "\n")
