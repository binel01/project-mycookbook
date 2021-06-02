# from typing import ClassVar
from django.forms import ModelForm, modelformset_factory
from django.forms.widgets import TextInput, Textarea

from .models import Cookbook, Recipe, Ingredient


class CookbookCreationForm(ModelForm):
    class Meta:
        model = Cookbook
        fields = ['name']


class RecipeCreationForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'guest', 'prep_time', 'cook_time', 'source']
        labels = {
            'title': 'Nom de la recette ',
            'description': 'Une description ',
            'guest': 'Pour combien de personne ',
            'prep_time': 'Temps de préparation ',
            'cook_time': 'Temps de cuisson ',
            'source': 'Source de la recette'
        }
        widgets = {
            'description': Textarea(attrs={'cols': 5, 'rows': 3}),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'measure', 'quantity']
        labels = {
            'name': 'Ingédient : ',
            'measure': 'La mesure : ',
            'quantity': 'La quantité : ',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nom', 'size': '20'}),
            'measure': TextInput(attrs={'placeholder': 'Mesure',  'size': '10'}),
            'quantity': TextInput(attrs={'placeholder': 'Quantité',  'size': '5'}),
        }

# IngredientFormSet = modelformset_factory(
#     Ingredient,
#     form=IngredientForm,
#     # extra=3,
# )
