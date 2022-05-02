from django.urls import path

from meal_plans.views import (
    MealPlanDeleteView,
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanUpdateView,
)


urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plans_list"),
    path("new/", MealPlanCreateView.as_view(), name="meal_plans_new"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="meal_plans_detail"),
    path(
        "<int:pk>/edit/", MealPlanUpdateView.as_view(), name="meal_plans_edit"
    ),
    path(
        "<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plans_delete",
    ),
]
