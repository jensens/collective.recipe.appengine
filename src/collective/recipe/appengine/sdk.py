import os
from hexagonit.recipe.download import Recipe as HRDRecipe


class Recipe(HRDRecipe):

    def __init__(self, buildout, name, options):
        parts_dir = os.path.abspath(buildout['buildout']['parts-directory'])
        options.setdefault('destination', os.path.join(parts_dir, name))
        options.setdefault('clear-destination', 'true')
        options.setdefault('download-only', 'false')
        options.setdefault('strip-top-level-dir', 'true')
        super(Recipe, self).__init__(buildout, name, options)
