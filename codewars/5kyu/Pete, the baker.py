def cakes(recipe, available):
    num_cakes = float('inf')

    for ingredient, amount_needed in recipe.items():
        if ingredient not in available:
            return 0
        num_possible = available[ingredient] // amount_needed
        if num_possible < num_cakes:
            num_cakes = num_possible

    return num_cakes


if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    cakes(recipe, available)
