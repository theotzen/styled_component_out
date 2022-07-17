# styled_component_out

This repository provides python code to **automatically create style files, add styled-components in, import and delete them in the react jsx file**. 

_____

This code is written for the most used way of using styled-components : 
```
components folder 
            |__component1            
                      |__ index.jsx                      
            |__component2
                      |__ index.jsx
            |__component3
                      |__ index.jsx
```                      
                      
With styled-components in each `index.jsx` file in the form : 
```
import styled from 'styled-components'

const Wrapper = styled.div`
	display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column; 
    height: 100%;
    width: 100%;	
`

 const SubWrapper = styled.div`
	display: inline;
	width: 80%;
`
```
                      
Running this code will ouput in the form : 

```
components folder 
            |__component1            
                      |__ index.jsx      
                      |__ style.jsx
            |__component2
                      |__ index.jsx
                      |__ style.jsx
            |__component3
                      |__ index.jsx
                      |__ style.jsx
```    

Where styled-components are imported in ìndex.jsx`, and `style.jsx`(or any other style file name) has the form : 

```
import styled from 'styled-components'

export const Wrapper = styled.div`
	display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column; 
    height: 100%;
    width: 100%;	
`

export const SubWrapper = styled.div`
	display: inline;
	width: 80%;
`
```
