import gradio as gr
from env.moderation_env import ModerationEnv
from env.models import Action

env = ModerationEnv("medium")
obs = env.reset()

def step_env(label, action, confidence):
    global obs
    act = Action(label=label, action=action, confidence=float(confidence))
    obs, reward, done, _ = env.step(act)

    status = "✅ Good Decision" if reward > 0.7 else "❌ Poor Decision"

    return obs.content, reward, done, str(obs.previous_actions), status

def reset_env():
    global obs
    obs = env.reset()
    return obs.content, 0, False, "[]", ""

with gr.Blocks() as demo:
    gr.Markdown("# 🛡️ AI Content Moderation Demo")

    content = gr.Textbox(label="Content", interactive=False)
    reward = gr.Number(label="Reward")
    done = gr.Checkbox(label="Done")
    history = gr.Textbox(label="Previous Actions")
    status = gr.Textbox(label="Status")

    with gr.Row():
        label = gr.Dropdown(["safe", "toxic", "spam", "abusive"], label="Label")
        action = gr.Dropdown(["allow", "warn", "remove"], label="Action")
        confidence = gr.Slider(0, 1, value=0.5)

    gr.Button("Step").click(step_env, inputs=[label, action, confidence],
                            outputs=[content, reward, done, history, status])

    gr.Button("Reset").click(reset_env,
                             outputs=[content, reward, done, history, status])

demo.launch()
