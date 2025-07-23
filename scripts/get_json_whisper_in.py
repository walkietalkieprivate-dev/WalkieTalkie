import json
text = "YEYEYEYEYEYEYEYE"
# Assume the input is called 'text' — ComfyUI will pass it as a function argument
def func(text):
    json_data = {"transcription": text}
    json_string = json.dumps(json_data, ensure_ascii=False, indent=2)
    return json_data, json_string

# Call the function with the input 'text'
# (The ComfyUI Python node usually injects variables with input names)
json_output, json_string = func(text)

# Return outputs as a dictionary
outputs = {
    "json_output": json_output,
    "json_string": json_string
}
print(outputs)