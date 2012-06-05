AutoCompleteInputs
------------------

Based on autocomplete from jquery-ui.

Use on the web
--------------

You have to load jquery, jquery-ui and if you want, a jquery-ui stylesheets.

Define your own Forms using the widget TextInputAutocomplete, for example::

  from django import forms
  from myapp.models import MyModel
  from autocompleteinputs.widgets import TextInputAutocomplete

  class MyAutocompleteForm(forms.Form):
      name = forms.CharField(widget=TextInputAutocomplete(attrs={'queryset': MyModel.objects.all(), 'value_field': 'name'}))

The you can use this form on your view like any other form.

If you want to use this with querysets knowed only when the view is loaded, you can "configure" the widget using the configure method::

  def myview(self, request, slug):
      obj = MyModel.objects.get(slug=slug)
      form = MyAutocompleteForm()
      queryset = obj.related_item.all()
      value_field = 'related_item_name'
      form.fields['name'].widget.configure(queryset, value_field)
      ...

Use on admin
------------

Yo have to overwrite the form for the admin like this::

  from django import forms
  from myapp.models import MyModel
  from autocompleteinputs.widgets import TextInputAutocomplete
  
  class MyModelForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super(MyModelForm, self).__init__(*args, **kwargs)
          self.fields['name'].widget = TextInputAutocomplete(attrs={'queryset': MyModel.objects.all(), 'value_field': 'name'})
  
      class Media:
          # Your path to jquery, jquery-ui and jquery-ui template
          css = { "all": ["css/ui-template/jquery-ui.css"], }
          js = ("js/libs/jquery.js","js/libs/jquery-ui.js",)

When you have this form you can use this form in the Admin class for this Model.
