from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import BlogPost


POSTS = [
    {
        "title": "Ipsum sur un texte générique comme 'Du texte. Du texte. Du texte.'",
        "sub_title": "De nombreuses suites logicielles de mise en page ou éditeurs de sites Web ont fait du Lorem Ipsum",
        "content": "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant "
                   "impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, "
                   "quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre "
                   "spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté "
                   "à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans "
                   "les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, "
                   "plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus "
                   "PageMaker. Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en "
                   "page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les "
                   "années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un "
                   "livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi "
                   "adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé "
                   "dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, "
                   "et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus "
                   "PageMaker",
    },
    {
        "title": "Contrairement à une opinion répandue, le Lorem Ipsum n'est pas simplement du texte aléatoire.",
        "sub_title": "source incontestable du Lorem Ipsum. Il provient en fait des sections 1.10.32 et 1.10.33 du De "
                     "Finibus Bonorum",
        "content": "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant "
                   "impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, "
                   "quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre "
                   "spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté "
                   "à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans "
                   "les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, "
                   "plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus "
                   "PageMaker. Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en "
                   "page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les "
                   "années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un "
                   "livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi "
                   "adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé "
                   "dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, "
                   "et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus "
                   "PageMaker. Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en "
                   "page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les "
                   "années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un "
                   "livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi "
                   "adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé "
                   "dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, "
                   "et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus "
                   "PageMaker. Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en "
                   "page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les "
                   "années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un "
                   "livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi "
                   "adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé "
                   "dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, "
                   "et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus "
                   "PageMaker",
    }
]


def create_post(author, title, sub_title, content):
    return BlogPost(author=author, title=title, sub_title=sub_title, content=content)


class Command(BaseCommand):

    author = User.objects.get(pk=1)

    def handle(self, *args, **options):
        self.stdout.write("Datas collection...")

        for post in POSTS:
            p = create_post(author=self.author, title=post["title"], sub_title=post["sub_title"],
                            content=post['content'])
            p.save()
            self.stdout.write(f"Post '{p.title[:15]}...' with content '{p.content[:20]}...' created")


