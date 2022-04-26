from django import forms

try:
    from tags.models import Tag

    class TagForm(forms.ModelForm):
        class Meta:
            model = Tag
            fields = [
                "name",
                "recipe",
            ]

except Exception:
    pass


from tags.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
