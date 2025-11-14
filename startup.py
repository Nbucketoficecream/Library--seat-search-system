import gradio as gr
import getting_api as ga
import pandas as pd

def search(branch):
   raw_data=ga.data_classiy(branch)
   data = [{"樓層": c["floorName"], "區域名稱": c["areaName"], "總座位": c["totalCount"], "可用座位": c["freeCount"]} for c in raw_data]
   return pd.DataFrame(data)
demo = gr.Interface(
    fn=search,
   inputs=[
        gr.Dropdown(
            ["總館", "稻香分館", "廣慈分館", "文山分館", "西湖分館"],
            label="選擇分館",
            info="請選擇要查詢的分館"
        ),
    ],
   outputs=gr.Dataframe(
        label="查詢結果",
        interactive=False,  
        row_count=(0, "fixed"),  
        col_count=(4, "fixed"), 
        wrap=True,               
        headers=["樓層", "區域名稱", "總座位", "可用座位"], 
    ),
    title="圖書座位查詢系統",
    allow_flagging="never"
)
demo.launch(server_name="0.0.0.0", server_port=7860)

