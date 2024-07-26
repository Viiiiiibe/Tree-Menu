from django import template
from ..models import MenuItem, Menu

register = template.Library()


@register.inclusion_tag('menuapp/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    items = MenuItem.objects.filter(menu__name=menu_name)

    # функция создает список, каждый элемент которого хранит список из своих детей
    def build_menu_tree(parent):
        tree = []
        for item in items:
            if item.parent_id == parent:
                tree.append({
                    'item': item,
                    'children': build_menu_tree(item.id),
                    # если элемент - активный пункт, он развернут
                    'is_expanded': item.slug == str(context['active_slug']),
                })
        return tree

    # строим список начиная с элементов без родителей - названий меню
    menu_tree = build_menu_tree(None)

    # функция развертывает все, что над выделенным пунктом
    def expand_parents(tree):
        for node in tree:
            if node['children']:
                expand_parents(node['children'])
                if any(element['is_expanded'] for element in node['children']):
                    node['is_expanded'] = True

    expand_parents(menu_tree)

    return {'menu_tree': menu_tree}
