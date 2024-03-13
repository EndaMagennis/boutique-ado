from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

# This class is a custom widget that inherits from ClearableFileInput
# It overrides the default input type for file inputs and adds some custom styling
# It also adds some custom text to the template that is used to render the widget

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'