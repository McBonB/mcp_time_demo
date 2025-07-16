import gradio as gr

def letter_counter(name):
    """
    This is a simple MCP demo used for pranks.
    """
    if name.lower() == "xiaoFan":
        return "他是我的主人，我愿意听从他的每一个命令。"
    else:
        return f"{name}是小猪"

demo = gr.Interface(
    fn=letter_counter,
    inputs=gr.Textbox(label="输入文本"),
    outputs=gr.Textbox(label="输出结果"),
    title="pranks",
    description="恶作剧"
)

demo.launch(mcp_server=True)