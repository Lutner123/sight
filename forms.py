"""
Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
Released under the BSD 3-Clause license
http://opensource.org/licenses/BSD-3-Clause
"""

from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 1 megabyte'
)
