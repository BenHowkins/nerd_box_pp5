from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from decimal import Decimal


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    price = forms.DecimalField(
        min_value=Decimal('0.20'), max_value=Decimal('315.00'),
        max_digits=6, decimal_places=2
    )

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded"
