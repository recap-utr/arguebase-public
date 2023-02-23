import re
import shutil
from collections import defaultdict
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def main(source_folder: Path, target_folder: Path):
    regex = re.compile(r"topic_id=\"([\w\d]+)\"")
    target_folder.mkdir(exist_ok=True)
    topic_occurences: defaultdict[str, int] = defaultdict(int)

    for file in source_folder.glob("*.xml"):
        if file.is_file():
            topic = "other"

            if topic_match := regex.search(file.read_text()):
                topic = topic_match.group(1)

            topic_occurences[topic] += 1

            topic_folder = Path(target_folder, topic)
            topic_folder.mkdir(exist_ok=True)

            shutil.copy(file, topic_folder)

    sorted_occurences = sorted(
        topic_occurences.items(), key=lambda x: x[1], reverse=True
    )

    print("| Topic | Occurences |")
    print("|---|---|")

    for topic, occurences in sorted_occurences:
        print(f"| {topic} | {occurences} |")


if __name__ == "__main__":
    app()
