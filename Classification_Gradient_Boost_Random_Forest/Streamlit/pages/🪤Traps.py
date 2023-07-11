import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


#Configurations
st.set_page_config(page_title='West Nile Virus', page_icon='🦟', layout='wide')
st.title('🦟West Nile Virus')


#the body of the page
def main():
    html_temp = """
    <div style="display: flex; justify-content: flex-start;">
    <div class='tableauPlaceholder' id='viz1688618623969' style='position: center'>
    <noscript>
        <a href='#'>
        <img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GA&#47;GAWestNileProject&#47;Dashboard1&#47;1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='GAWestNileProject&#47;Trapsdashboard' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GA&#47;GAWestNileProject&#47;Dashboard1&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object>
    </div>
    <script type='text/javascript'>
    var divElement = document.getElementById('viz1688618623969');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {
        vizElement.style.width = '1000px';
        vizElement.style.height = '827px';
    } else if (divElement.offsetWidth > 500) {
        vizElement.style.width = '1000px';
        vizElement.style.height = '827px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = '1700px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>

    """
    components.html(html_temp, width=1100, height=1210)
    st.markdown(f'Link to the public dashboard [here](https://public.tableau.com/app/profile/altheaxcvii/viz/GAWestNileProject/Trapsdashboard)')

    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)

# the controller
def load_page():
    main()


if __name__ == "__main__":
    load_page()