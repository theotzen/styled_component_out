from utils import *


def write_style_for_one_folder(folder: str, style_imports="import styled from 'styled-components'", react_file_name="index.jsx",
                               style_file_name="style.jsx", verbose=True):
    """
    Creates a style file, writes styled-components, deletes styled-components from react-file and imports styled-components in react-file for 
        all subfolders in input folder
                                    Parameters:
                                        folder (str): the path of the folder with all subfolders
                                        style_imports (str): style import to write in all style file
                                        react_file_name (str): the react file in the folder. Usually index.jsx
                                        style_file_name (str): name of the style file. Usually style.jsx
                                        verbose (bool): boolean to conditionaly log info

                                    Returns:
    """
    for path in get_subfolders_from_folder(folder):
        create_style_file_in_one_subfolder(
            path, style_file_name=style_file_name, imports=style_imports)
        style_constants = get_style_to_write(
            path, react_file_name=react_file_name)  # get all style constants

        if style_constants != '':
            importToWrite = build_imports_from_style(
                style_components_string=style_constants, style_file_name=style_file_name)  # create import { } from 'style.jsx'
            to_write = style_imports + '\n' + style_constants
            # write the style constants + import in style.jsx
            write_styled_in_style_file(
                path, style_to_write=to_write, style_file_name=style_file_name, verbose=verbose)
            # delete style const in index.jsx
            delete_style_consts(path, style_written_in_style_file=style_constants,
                                react_file_name=react_file_name, verbose=verbose)
            # add style import in index.jsx
            add_style_import(path=path, imports=importToWrite,
                             react_file_name=react_file_name, verbose=verbose)

    return None


def write_style_for_each_folder(folders, style_imports=["import styled from 'styled-components'"], react_file_names=["index.jsx"],
                                style_file_names=["style.jsx"], verbose=True):
    """
    Creates a style file, writes styled-components, deletes styled-components from react-file and imports styled-components in react-file for 
        all subfolders in each folder in input folders
                                    Parameters:
                                        folders list(str): the path of the folders with all subfolders
                                        style_imports list(str): style import to write in all style file, for each folder
                                        react_file_name list(str): the react file in the folder, for each folder. Usually index.jsx
                                        style_file_name list(str): name of the style file, for each folder. Usually style.jsx
                                        verbose (bool): boolean to conditionaly log info

                                    Returns:
    """
    number_of_folders = len(folders)
    if len(style_imports) == 1:
        style_imports = style_imports*number_of_folders
    elif len(style_imports) < number_of_folders:
        logging.exception("Inputs must have the same length as folders")
    if len(react_file_names) == 1:
        react_file_names = react_file_names*number_of_folders
    elif len(react_file_names) < number_of_folders:
        logging.exception("Inputs must have the same length as folders")
    if len(style_file_names) == 1:
        style_file_names = style_file_names*number_of_folders
    elif len(style_file_names) < number_of_folders:
        logging.exception("Inputs must have the same length as folders")

    for i in range(number_of_folders):
        write_style_for_one_folder(folders[i], style_imports=style_imports[i],
                                   react_file_name=react_file_names[i], style_file_name=style_file_names[i], verbose=verbose)
