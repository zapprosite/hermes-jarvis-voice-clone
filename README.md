# hermes-jarvis-voice-clone

**Voice models para o kit Hermes Jarvis SOTA v2.**

Contém os 2 modelos de voz essenciais do kit:

1. **Wake model** (`models/jarvis_ptbr_user.onnx`) — OWW custom treinado em PT-BR (Will's voice)
2. **TTS voice** (`models/jarvis-clone-trimmed.wav`) — OmniVoice TTS voice clonada

## Install

```bash
pip install hermes-jarvis-voice-clone
```

## Install models (download + SHA256 validation)

```python
from hermes_jarvis_voice_clone import install_models
install_models(target_dir="/usr/local/share/hermes-jarvis-voice-clone/models")
```

## Como usar

Ver [MODELS.md](MODELS.md) para detalhes de cada modelo (SHA256, threshold, etc).

## Compatibilidade

- Python 3.11+
- NVIDIA RTX 3060+ (CUDA 12+)
- Ubuntu 22.04+

## License

MIT — modelos são do Will e podem ser usados livremente.

Refs: STATE_MANIFEST.md, MINIMAL_VIABLE_REPO.md
