import logging
import os
import re


def build_imports_from_style(style_components_string: str, style_file_name="style.jsx") -> str:
    """
    Returns the import string to paste in the jsx file : import { style_component } from './style_file.jsx
                Parameters:
                                style_components_string (str): all styled_components in one string
                                style_file_name (str): style_file_name, usually style.jsx

                Returns:
                                imports (str): import string
    """
    style_components_string.replace('export ', '')
    splittedStyle = style_components_string.split('const')
    imports = "import { "
    for style in splittedStyle:
        if len(style) > 2 and "=" in style:
            imports += style.split("=")[0].strip()
            imports += ", "
    imports += f"}} from './{style_file_name}' "
    return imports


style_imports = '''
import styled from 'styled-components'
import colors from '../../utils/style/colors'
import { Link } from 'react-router-dom'
'''


def get_subfolders_from_folder(folder: str):
    """
    Returns a list of all subfolders for the inphut folder
                            Parameters:
                                    folder (str): path to the folder to get the subfolders from

                            Returns:
                                    subfolders (list(str)): list of subfolders
    """
    return [f.path for f in os.scandir(folder) if f.is_dir()]


def create_style_file_in_each_subfolder(folder: str, style_file_name="style.jsx", imports="import styled from 'styled-components'"):
    """
    Creates a style file with style_file_name in each subfolder of the input folder. The style file can be initialized with basic imports.
                    Parameters:
                                    folder (str): path to the folder to create style file in its subfolders
                                    style_file_name (str): the style file name. Usually style.jsx
                                    imports (str): imports to write in style file

                    Returns:
    """
    subfolders = get_subfolders_from_folder(folder)
    for path in subfolders:
        create_style_file_in_one_subfolder(
            path, style_file_name=style_file_name, imports=imports)


def create_style_file_in_one_subfolder(subfolder: str, style_file_name="style.jsx", imports="import styled from 'styled-components'"):
    """
    Creates a style file with style_file_name in input subfolder. The style file can be initialized with basic imports.
                    Parameters:
                                    subfolder (str): path to the subfolder to create style file in 
                                    style_file_name (str): the style file name. Usually style.jsx
                                    imports (str): imports to write in style file

                    Returns:
    """
    file_to_create = subfolder + f"/{style_file_name}"
    with open(file_to_create, 'w') as f:
        f.write(imports)
        f.close()


def get_all_styled_const(data: str):
    """
    Returns a list of all styled-component constants
                            Parameters:
                                    data (str): the entire .jsx file containing react code and style components

                            Returns:
                                    styled_constants (list(str)): list of all styled-component constants
    """
    return [x for x in re.split(r'(function|class)', data)[0].split('const')[1:] if 'styled' in x]


def get_style_to_write(path: str, react_file_name="index.jsx"):
    """
    Returns a string with all the style to write in the style file
                            Parameters:
                                path (str): the path of the folder with the react and the style file
                                react_file_name (str): the react file in the folder. Usually index.jsx

                            Returns:
                                style_to_write (str): a string with all the style to write in the style file
    """
    pathIndex = path + f"/{react_file_name}"
    try:
        text_file = open(pathIndex, "r")
    except:
        logging.warning(f"Could not open file {pathIndex}")
        return ''
    data = text_file.read()
    text_file.close()
    styled_constants = get_all_styled_const(data)
    if len(styled_constants) == 0:
        logging.warning(f"Could not find any style in file {pathIndex}")
        return ''
    styled_constants[0] = 'export const' + styled_constants[0]
    to_write = 'export const'.join(styled_constants)
    return to_write


def write_styled_in_style_file(path: str, style_to_write: str, style_file_name="style.jsx", verbose=True):
    """
    Writes the exported style constants in the style file.
                            Parameters:
                                path (str): the path of the folder with the react and the style file
                                style_to_write (str): the react file in the folder. Usually index.jsx
                                style_file_name (str): name of the style file. Usually style.jsx
                                verbose (bool): boolean to conditionaly log info

                            Returns:
    """
    file_to_writeIn = path + f"/{style_file_name}"
    try:
        with open(file_to_writeIn, 'w') as f:
            f.write(style_to_write)
        if verbose:
            logging.info(f"Style wrote in file {file_to_writeIn}")
    except:
        logging.warning(f"Could not write style in file {file_to_writeIn}")
    return None


def add_style_import(path: str, imports: str, react_file_name="index.jsx", verbose=True):
    """
    Writes the import for styled components in react file.
                                Parameters:
                                    path (str): the path of the folder with the react and the style file
                                    imports (str): the import string. import { ... } from './style.jsx'
                                    react_file_name (str): the react file in the folder. Usually index.jsx
                                    verbose (bool): boolean to conditionaly log info

                                Returns:
    """
    pathIndex = path + f'/{react_file_name}'
    text_file = open(pathIndex, "r")
    data = text_file.read()
    text_file.close()
    all_together = imports + '\n' + data
    try:
        with open(pathIndex, 'w') as f:
            f.write(all_together)
        if verbose:
            logging.info(f"Imports wrote in file {pathIndex}")
    except:
        logging.warning(f"Could not write imports in file {path}")
    return None


def delete_style_consts(path, style_written_in_style_file, react_file_name="index.jsx", verbose=True):
    """
    Deletes style-components constants in react file by rewriting the file without.
                                Parameters:
                                    path (str): the path of the folder with the react and the style file
                                    style_written_in_style_file (str): string containing all styled components
                                    react_file_name (str): the react file in the folder. Usually index.jsx
                                    verbose (bool): boolean to conditionaly log info

                                Returns:
    """
    style_written_in_style_file = style_written_in_style_file.replace(
        'export ', '')
    pathIndex = path + f"/{react_file_name}"
    try:
        text_file = open(pathIndex, "r")
    except:
        logging.warning(f"Could not open file {pathIndex}")
        return None
    data = text_file.read()
    text_file.close()
    if (style_written_in_style_file not in data):
        logging.warning(
            f"Could not find styled constants in file {pathIndex}")
        return None
    data = data.replace(style_written_in_style_file, '')
    try:
        with open(pathIndex, 'w') as f:
            f.write(data)
        if verbose:
            logging.info(f"Styled-constants deleted from file {pathIndex}")
    except:
        logging.warning(f"Could not delete styled-constants from file {path}")
    return None
