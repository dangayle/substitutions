substitutions
=============

Django template filter to implement <http://xkcd.com/1288/>

![](http://imgs.xkcd.com/comics/substitutions.png)


Usage
-----

Add it to your installed apps:

```python
INSTALLED_APPS = (
    ...
    'substitutions',
    ...
)
```

In your template, load the template tags and add `substitute` as a filter:

```html
{% load substitutions %}

{% block content %}
<h1>{{ post.title }}</h1>
<p>{{ post.content|substitute }}</p>
{% endblock %}
```

TODO
-----

- [x] Basic tests
- [] Word boundaries!
- [] Make `pip` installable


License
-------
MIT
