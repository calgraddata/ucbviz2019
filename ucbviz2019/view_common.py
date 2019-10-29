import dash_html_components as html
import dash_core_components as dcc


def nav_html():
    by_degree = dcc.Link(
        "Explore by Degree Program", href="/by_degree", className="navbar-item"
    )
    by_analysis = dcc.Link(
        "Explore Analyses", href="/by_analysis", className="navbar-item"
    )
    about = dcc.Link(
        "About", href="/by_about", className="navbar-item"
    )
    navbar_start = html.Div(
        [by_degree, by_analysis, about], className="navbar-start"
    )

    log_in = html.A(
        "",
        className="button is-dark is-small is-hidden",
    )
    buttons = html.Div(log_in, className="buttons")
    buttons_item = html.Div(buttons, className="navbar-item")
    navbar_end = html.Div(buttons_item, className="navbar-end")

    navbar_menu_id = "core-navbar-menu"
    navbar_menu = html.Div(
        [navbar_start, navbar_end], id=navbar_menu_id, className="navbar-menu"
    )

    nav_image = html.Img(src="/assets/logo.png", height=300)
    nav_image_container = html.A(
        nav_image,
        className="navbar-item",
    )

    burger = html.Span(**{"aria-hidden": True})
    nav_burger = html.A(
        [burger] * 3,
        id="core-burger-trigger-cs",
        role="button",
        className="navbar-burger",
        **{
            "aria-label": "menu",
            "aria-expanded": False,
            "data-target": navbar_menu_id,
        }
    )
    navbar_brand = html.Div(
        [nav_image_container, nav_burger], className="navbar-brand"
    )

    nav_menu = html.Div(
        [navbar_brand, navbar_menu],
        className="navbar is-link is-fixed-top",
        role="navigation",
        **{"aria-label": "main navigation"}
    )
    nav_with_padding = html.Div(nav_menu, className="has-navbar-fixed-top")
    return nav_with_padding


def common_404_html():
    return html.Div("404", className="is-size-3 has-text-centered")


def common_info_box_html(elements, id=None):
    """
    Get an outlined box for displaying information, such as references, about
    page stuff, etc. Can be used in any app.

    Args:
        elements ([dash_html_components.Div], dash_html_components.Div): Either
            a single dash html component or multiple in a list. These will
            be encapsulated by the box.
        id (str, None): The id you want to assign to the container of the box.

    Returns:
        container (dash_html_components.Div): an html block container for the
            box encapsulating your elements.

    """
    element_container = html.Div(elements, className="has-margin-30")
    box = html.Div(element_container, className="box")
    column = html.Div(box, className="column is-two-thirds")
    columns = html.Div(
        column, className="columns is-centered has-margin-top-50"
    )
    container = html.Div(columns, className="container", id=id)
    return container


def common_info_box_wide_html(elements, id=None):
    """
    Get an outlined box for displaying information, such as references, about
    page stuff, etc. Can be used in any app.

    Args:
        elements ([dash_html_components.Div], dash_html_components.Div): Either
            a single dash html component or multiple in a list. These will
            be encapsulated by the box.
        id (str, None): The id you want to assign to the container of the box.

    Returns:
        container (dash_html_components.Div): an html block container for the
            box encapsulating your elements.

    """
    element_container = html.Div(elements, className="has-margin-30")
    box = html.Div(element_container, className="box")
    column = html.Div(box, className="column is-three-fourths")
    columns = html.Div(
        column, className="columns is-centered has-margin-top-50"
    )
    container = html.Div(columns, className="container", id=id)
    return container