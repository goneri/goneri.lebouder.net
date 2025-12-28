+++
title = "Ollama: apply a Lora on a model"
date = 2025-04-30T18:46:31+00:00
+++
First, I've prepared a Lora with [Axolotl](https://github.com/axolotl-ai-cloud/axolotl):

```
axolotl train examples/llama-3/lora-1b.yml
```

At the end of the process, I've a new directory called `outputs/lora-out`.

I now need to prepare a new model that will be a mix of an Original Llama3 model and this new file called `llama3.1-modelfile`:

```
FROM llama3.2:1b

ADAPTER /home/ec2-user/axolotl/outputs/lora-out
```

Finally, I can prepare my local model with:

`ollama create llama3_with_lora -f llama3.1-modelfile`

The operation lasts a couple of seconds and I can now start a new Chat:

`ollama run llama3_with_lora`
