from django.urls import path


from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    create_shopping_item,
    log_rating,
    RecipeDetailView,
    RecipeListView,
    ShoppingItemListView,
    delete_all_shopping_items,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path(
        "shopping_items/",
        ShoppingItemListView.as_view(),
        name="ShoppingItem_list",
    ),
    path("create_shopping/", create_shopping_item, name="shoppingitem"),
    path(
        "shopping_items/delete",
        delete_all_shopping_items,
        name="delete_all_shopping_items",
    ),
]
