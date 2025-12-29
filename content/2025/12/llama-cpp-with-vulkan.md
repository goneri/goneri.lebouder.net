+++
title = "Llama.cpp with Vulkan"
date = 2025-12-06T16:45:56+00:00
+++
Running Llama.cpp with the Vulkan backends of my AMD and Intel graphic GPUs ends up being straightfoward and surprisingly fast.

Build you container with:

```
podman build -t llama-cpp-vulkan --target server -f .devops/vulkan.Dockerfile .
```

and run it with:

```
podman run -it --rm --security-opt seccomp=unconfined --device /dev/dri:/dev/dri --volume ~/.cache:/root/.cache:z -p 8080:8080 localhost/llama-cpp-vulkan -hf Qwen/Qwen3-Embedding-8B-GGUF --embeddings
```

In the example above, I reuse my \~/.cache directory and I use the model to compute embeddings, thus the `--embeddings`.
