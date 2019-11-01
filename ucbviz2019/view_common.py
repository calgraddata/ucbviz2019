import dash_html_components as html
import dash_core_components as dcc


def nav_html(page="/"):
    common_nav_item_style = "navbar-item"


    by_degree_style = common_nav_item_style
    by_analysis_style = common_nav_item_style
    about_style = common_nav_item_style

    highlighted_style = " has-text-weight-semibold"
    if page in ["/", "/by_degree"]:
        by_degree_style += highlighted_style
    elif page=="/by_analysis":
        by_analysis_style += highlighted_style
    elif page == "/by_about":
        about_style += highlighted_style

    by_degree = dcc.Link(
        "Explore by Degree Program", href="/by_degree", className=by_degree_style
    )
    by_analysis = dcc.Link(
        "Explore Trends", href="/by_analysis", className=by_analysis_style
    )
    about = dcc.Link(
        "About", href="/by_about", className=about_style
    )
    navbar_start = html.Div(
        [by_degree, by_analysis, about], className="navbar-start"
    )

    log_in = html.A(
        "",
        className="button is-dark is-small is-hidden",
    )
    buttons = html.Div(log_in, className="buttons")
    buttons_item = html.Div(buttons, className="navbar-item is-hidden")
    navbar_end = html.Div(buttons_item, className="navbar-end")

    navbar_menu_id = "core-navbar-menu"
    navbar_menu = html.Div(
        [navbar_start, navbar_end], id=navbar_menu_id, className="navbar-menu ucbvc-background-grey"
    )

    nav_image = html.Img(src="/assets/logo.png", height=300)
    nav_image_container = html.A(
        nav_image,
        href="/by_about",
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
        className="navbar ucbvc-background-dark-blue is-fixed-top",
        role="navigation",
        **{"aria-label": "main navigation"}
    )
    nav_with_padding = html.Div(nav_menu, className="has-navbar-fixed-top")
    return nav_with_padding


def common_404_html():
    return html.Div("404", className="is-size-3 has-text-centered")


def common_info_box_html(elements):
    """
    Get an outlined box for displaying information, such as references, about
    page stuff, etc. Can be used in any app.

    Args:
        elements ([dash_html_components.Div], dash_html_components.Div): Either
            a single dash html component or multiple in a list. These will
            be encapsulated by the box.

    Returns:
        container (dash_html_components.Div): an html block container for the
            box encapsulating your elements.

    """
    element_container = html.Div(children=elements, className="has-margin-20")
    box = html.Div(children=[element_container], className="box")
    column = html.Div(children=[box], className="column is-three-fourths")
    columns = html.Div(
        children=[column], className="columns is-centered has-margin-top-30"
    )
    container = html.Div(children=[columns], className="container")
    return container


def wrap_in_loader_html(element):
    """
    Wrap the elements in a common loading element.

    Args:
        elements: The element MUST be updated via callback DIRECTLY to work.

    Returns:

    """
    return dcc.Loading(
        # 'graph', 'cube', 'circle', 'dot', 'default'
        # type="cube",
        children=element,
        className="ucbvc-fade-in has-margin-top-50 has-margin-bottom-50"
    )

common_plotly_graph_font_style = dict(family="Condo")
common_header_style = "is-size-4 has-margin-10 has-text-weight-semibold"
common_explanation_style = "is-size-6 has-margin-10"