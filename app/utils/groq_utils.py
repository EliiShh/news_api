import ast


def convert_groq_to_dict(str_to_dict):
    start_index = str_to_dict.find("{")
    end_index = str_to_dict.rfind("}")
    if start_index != -1 and end_index != -1:
        dict_str = str_to_dict[start_index:end_index + 1]
        try:
            n = ast.literal_eval(dict_str)
            r, c, ci = n['region_txt'], n['country_txt'], n["city_name"]
            return {'region_txt': n.get('region_txt'), 'country_txt': n.get('country_txt'), 'city_name': n.get('city_name')}
        except (ValueError, SyntaxError, KeyError, Exception):
            return {'region_txt':None, 'country_txt':None, "city_name": None}



