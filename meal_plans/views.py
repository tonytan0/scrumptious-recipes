from django import views
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from meal_plans.models import MealPlan


# Create your views here.


class MealPlanListView(ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"
    paginate_by = 3

    # def get_queryset(self):
    #     return MealPlan.objects.filter(over=self.request.user)


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "date", "owner", "recipes"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("meal_plans_detail", pk=plan.id)


class MealPlanDetailView(DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"

    def get_queryset(self, **kwargs):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "owner", "recipes"]

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def get_success_url(self) -> str:
        return reverse_lazy("meal_plans_detail", args=[self.object.id])


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_planss/delete.html"
    success_url = reverse_lazy("meal_plans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
