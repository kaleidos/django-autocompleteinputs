from django.template import Template, Context
from django.forms import TextInput
from django.utils.safestring import mark_safe

class TextInputAutocomplete(TextInput):
    def __init__(self, attrs=None):
        super(TextInputAutocomplete, self).__init__(attrs)
        self.queryset = self.attrs.pop('queryset', None)
        self.value_field = self.attrs.pop('value_field', None)

    def configure(self, queryset, value_field):
        self.queryset = queryset
        self.value_field = value_field

    def render(self, name, value, attrs=None):
        normal_widget = super(TextInputAutocomplete, self).render(name, value, attrs)

        if self.queryset:
            choices_widget_tpl = Template('''
            <script>
                $(document).ready(function(){
                    $("#id_{{name}}").autocomplete({
                        'startLength': 1,
                        'source': [
                              {% for item in item_list %}
                                  "{{item}}"{% if not forloop.last %},{% endif %}
                              {% endfor %}
                            ]
                    });                
                });
            </script>''')
            context = Context()
            context['name'] = name
            context['item_list'] = []

            for item in self.queryset.all():
                if self.value_field:
                    context['item_list'].append(getattr(item, self.value_field))
                else:
                    context['item_list'].append(unicode(item))

            choices_widget = choices_widget_tpl.render(context)
        else:
            choices_widget = ''
        return mark_safe(normal_widget + choices_widget)
