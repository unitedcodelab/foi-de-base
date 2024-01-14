import random, string

from ..models import Post


def create_slug(**post):
    title = post["title"]
    slug = title.lower()
    for letter in slug:
        if letter == " ":
            slug = slug.replace(letter, "-")
        elif not letter.isalpha():
            slug = slug.replace(letter, "")

    existing_slugs = Post.objects.filter(slug__startswith=slug).values_list("slug", flat=True)
    
    while slug in existing_slugs:
        random_string = "".join(random.choices(string.ascii_lowercase, k=16))
        slug += "-" + random_string

    return slug
