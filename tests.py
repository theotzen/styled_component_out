import unittest
from utils import *


class Testing(unittest.TestCase):
    def test_build_imports(self):
        style_file = '''
				import styled from 'styled-components'

				export const Wrapper = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: row;
					justify-content: space-between;
					align-items: center;
					padding: 5px 10px;
					gap: 91px;
					margin: 5px;
					width: 95%;
					height: 47px;
					/* Tons secondaires/Gris clair */
					background: #F9F9F9;
					border-radius: 10px;
				`

				export const LeftPart = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: row;
					justify-content: flex-start;
					align-items: center;
					padding: 0px;
					gap: 75px;
					width: 60%;
					height: 36px;
					/* Inside auto layout */
					flex: none;
					order: 0;
					flex-grow: 0;
				`

				export const NameLogoProject = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: row;
					justify-content: center;
					align-items: center;
					padding: 0px;
					gap: 25px;
					width: 157px;
					height: 36px;
					/* Inside auto layout */
					flex: none;
					order: 0;
					flex-grow: 0;
				`

				export const NameProject = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: column;
					align-items: flex-start;
					justify-content: center;
					padding: 0px;
					overflow: none;
					width: 109px;
					height: 36px;
					/* Inside auto layout */
					flex: none;
					order: 1;
					flex-grow: 0;
				`

				export const Name = styled.div`
					width: auto;
					height: 18px;
					font-family: 'Lato';
					font-style: normal;
					font-weight: 700;
					font-size: 14px;
					line-height: 148%;
					white-space: nowrap;
					/* identical to box height, or 18px */
					/* Tons secondaires/bleu foncé */
					color: #051138;
					/* Inside auto layout */
					flex: none;
					order: 0;
					flex-grow: 0;
				`

				export const ProjectName = styled.div`
					width: auto;
					height: 18px;
					font-family: 'Lato';
					font-style: normal;
					font-weight: 400;
					font-size: 12px;
					white-space: nowrap ;
					/* identical to box height, or 18px */
					/* Tons secondaires/bleu foncé */
					color: #051138;
					/* Inside auto layout */
					flex: none;
					order: 1;
					flex-grow: 0;
				`

				export const DateDiv = styled.div`
					width: 110px;
					height: 18px;
					font-family: 'Lato';
					font-style: normal;
					font-weight: 400;
					font-size: 12px;
					line-height: 148%;
					/* identical to box height, or 18px */
					text-transform: uppercase;
					/* Tons secondaires/Gris moyen */
					color: #C6C6C6;
					/* Inside auto layout */
					flex: none;
					order: 1;
					flex-grow: 0;
				`

				export const RightPartTransac = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: row;
					justify-content: center;
					align-items: center;
					padding: 0px;
					gap: 14px;
					width: 35%;
					height: 27px;
					font-family: 'Lato';
					font-style: normal;
					font-weight: 700;
					font-size: 18px;
					line-height: 148%;
					/* identical to box height, or 27px */
					/* Couleurs de fonction/Orange/green */    
					${({ isSent }) => isSent && `
						color: #FFA53A;
					`}
					${({ isSent }) => !isSent && `
						color: #69E9BB;
				`}
					/* Inside auto layout */
					flex: none;
					order: 1;
					flex-grow: 0;
				`

				export const RightPart = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: row;
					justify-content: center;
					align-items: center;
					padding: 0px;
					gap: 14px;
					width: 35%;
					height: 27px;
					font-family: 'Lato';
					font-style: normal;
					font-weight: 700;
					font-size: 14px;
					line-height: 148%;
					/* identical to box height, or 27px */
					/* Couleurs de fonction/Orange/green */    
					color: black;
					/* Inside auto layout */
					flex: none;
					order: 1;
					flex-grow: 0;
				`

				export const TagsBar = styled.div`
					/* Auto layout */
					display: flex;
					flex-direction: row;
					align-items: flex-start;
					padding: 0px;
					gap: 6px;
					width: auto;
					height: 16px;
					/* Inside auto layout */
					flex: none;
					order: 1;
					flex-grow: 0;
				`

				export const Tags = styled.div`
				box-sizing: border-box;
					/* Auto layout */
					display: flex;
					flex-direction: row;
					justify-content: center;
					align-items: center;
					padding: 2px 8px;
					width: auto;
					height: 16px;
					/* Tons secondaires/blanc */
					background: #FFFFFF;
					${({ isRecent }) => isRecent && `
						background: #69E9BB;
					`}
					/* Tons secondaires/bleu marine */
					border: 0.5px solid #132968;
					border-radius: 10px;
					/* Inside auto layout */
					flex: none;
					order: 0;
					flex-grow: 0;
					font-family: 'Lato';
					font-style: normal;
					font-weight: 400;
					font-size: 12px;
					line-height: 148%;
					/* identical to box height, or 12px */
					text-align: center;
				`
				'''
        computed_imports = build_imports_from_style(style_components_string=style_file,
                                                    style_file_name="style.jsx")
        imports = "import { Wrapper, LeftPart, NameLogoProject, NameProject, Name, ProjectName, DateDiv, RightPartTransac, RightPart, TagsBar, Tags, } from './style.jsx' "
        self.assertEqual(computed_imports, imports)


if __name__ == '__main__':
    unittest.main()
