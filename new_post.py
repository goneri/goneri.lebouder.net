#!/usr/bin/env python3
"""Create a new blog post for the Zola-based blog."""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


def slugify(title: str) -> str:
    """Convert a title to a URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def create_post(title: str) -> Path:
    """Create a new blog post with the given title."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    year = now.strftime("%Y")
    month = now.strftime("%m")

    slug = slugify(title)
    content_dir = Path(__file__).parent / "content" / "posts"
    year_dir = content_dir / year
    month_dir = year_dir / month
    post_dir = month_dir / slug

    # Create year/month/slug directory
    post_dir.mkdir(parents=True, exist_ok=True)

    # Create _index.md for the year if it doesn't exist
    year_index = year_dir / "_index.md"
    year_index.write_text("+++\ntransparent = true\n+++\n")

    # Create _index.md for the month if it doesn't exist
    month_index = month_dir / "_index.md"
    month_index.write_text("+++\ntransparent = true\n+++\n")

    # Create the post file as index.md inside the slug directory
    post_file = post_dir / "index.md"

    if post_file.exists():
        print(f"Error: Post already exists at {post_file}", file=sys.stderr)
        sys.exit(1)

    content = f"""+++
title = "{title}"
date = {date_str}
+++

"""

    post_file.write_text(content)
    print(post_file)

    return post_file


def main():
    parser = argparse.ArgumentParser(
        description="Create a new blog post",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  %(prog)s "My New Post Title"
""",
    )
    parser.add_argument("title", help="Title of the new blog post")

    args = parser.parse_args()
    create_post(args.title)


if __name__ == "__main__":
    main()
