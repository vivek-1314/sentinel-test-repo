from web.views import render_home, render_cart


def test_home():
    assert render_home("viv") == "<h1>Welcome viv</h1>"


def test_cart():
    assert render_cart(["a"]) == "<ul><li>a</li></ul>"
