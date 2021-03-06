__author__ = 'lottiwang'
import pandas as pb
import time
from IPython.display import HTML, Javascript




def highlight_last_row(s):
    return ['background-color: #FF0000' if i==len(s)-1 else '' for i in range(len(s))]

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if "SELL" in val else 'green'
    return 'color: %s' % color

def color_negative_red_num(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val >= 0 else 'green'
    return 'color: %s' % color
    


def csv_to_html():
    df = pb.read_csv("data/us_market.csv")
    df['operation']="BUY"
    html = (
    df.style
    .applymap(color_negative_red, subset=['operation'])
    .set_properties(**{'font-size': '11pt', 'font-family': 'Calibri','align':'center', 'border-style':'solid', 'border-width':'1px','border-color': 'gray','border-spacing':'0px'})
    .set_caption("Quant From Gua")
    .set_table_styles(\
        [{'selector': '.row_heading',\
          'props': [('display', 'none')]},\
         {'selector': '.blank.level0',\
          'props': [('display', 'none')]}])
    .render()
)
    print(html)
    with open("test.html",'w') as f:
        f.write(html)
        f.close()
        
        
def df_to_htmlfile(df):
    html = (
    df.style
    .applymap(color_negative_red_num,subset=['KDJ','DMI2','MACROSS','MACD','NEWHIGH'])
    .set_properties(**{'font-size': '7pt', 'font-family': 'Calibri','align':'center', 'border-style':'solid', 'border-width':'1px','border-color': 'gray','border-spacing':'0px'})
    .set_caption("Quant From Gua")
    .render()
)
    with open('data/QuantRet'+ '_' + time.strftime('%Y%m%d',time.localtime(time.time())) + '.html','w') as f:
        f.write(html)
        f.close()
        
def df_to_html(df):    
    html = (
    df.style
    .applymap(color_negative_red, subset=['operation'])
    .set_properties(**{'font-size': '11pt', 'font-family': 'Calibri','align':'center', 'border-style':'solid', 'border-width':'1px','border-color': 'gray','border-spacing':'0px'})
    .set_caption("Quant From Gua")
    .set_table_styles(\
    [{'selector': '.row_heading',\
      'props': [('display', 'none')]},\
     {'selector': '.blank.level0',\
      'props': [('display', 'none')]}])
    .render()
     )
    return html


if __name__ == "__main__":
	csv_to_html()











