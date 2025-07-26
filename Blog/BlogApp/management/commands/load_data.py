from django.core.management.base import BaseCommand
from BlogApp.models import Article

class Command(BaseCommand):
    help = 'Load initial data'

    def handle(self, *args, **options):
        if Article.objects.filter(title="Milk Cookiess").exists():
            self.stdout.write('Przepis "Milk Cookies" już istnieje!')
            return

        text = """🥛 Milk Cookies Recipe

Ingredients:
- 1 cup (225 g) unsalted butter, softened
- 3/4 cup (150 g) granulated sugar
- 1/4 cup (60 ml) milk
- 1 teaspoon vanilla extract
- 2 1/2 cups (315 g) all-purpose flour
- 1/2 teaspoon baking powder
- 1/4 teaspoon salt

Instructions:
1. Preheat oven to 350°F (175°C). Line a baking sheet with parchment paper.
2. In a large bowl, cream the butter and sugar together until light and fluffy.
3. Add the milk and vanilla extract, and mix well.
4. In another bowl, whisk together the flour, baking powder, and salt.
5. Gradually add the dry ingredients to the wet mixture, mixing until a soft dough forms.
6. Scoop tablespoon-sized portions and roll into balls. Flatten slightly with your hand or a fork.
7. Place on the prepared baking sheet, spacing them about 2 inches apart.
8. Bake for 10–12 minutes, or until the edges are lightly golden.
9. Let the cookies cool on a wire rack before serving."""

        article = Article.objects.create(
            title="Milk Cookies",
            text=text,
            img="images/Cookie.png",
            key_words=["Cookie", "Milk Cookie"]
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Pomyślnie dodano: {article.title}')
        )