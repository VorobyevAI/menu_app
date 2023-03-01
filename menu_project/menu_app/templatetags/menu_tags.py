from django import template
from menu_app.models import CategoriesMenu, Menu


register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu):

    try:
        items = CategoriesMenu.objects.filter(category__title=menu)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        parents_id_list = get_parents_list(primary_item)

        for item in primary_item:
            if item['id'] in parents_id_list:
                item['child_items'] = get_child_items(items_values, item['id'], parents_id_list)
        result_dict = {'items': primary_item}

    except:
        result_dict = {
            'items': [
                item for item in CategoriesMenu.objects.filter(category__title=menu, parent=None).values()
                ]
            }

    result_dict['menu'] = menu
    result_dict['q'] = get_querystring(context, menu)

    return result_dict


def get_querystring(context, menu):
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])

    querystring = ('q').join(querystring_args)
    return querystring


def get_child_items(items_values, current_item_id, selected_item_id_list):
    item_list = [item for item in items_values.filter(parent_id=current_item_id)]
    for item in item_list:
        if item['id'] in selected_item_id_list:
            item['child_items'] = get_child_items(items_values, item['id'], selected_item_id_list)
    return item_list


def get_parents_list(primary_item):
    parents_id_list = []
    for item in primary_item:
        parents_id_list.append(item['id'])
    return parents_id_list

