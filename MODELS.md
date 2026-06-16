# Voice Models — Jarvis Clone

## 1. Wake Model (OWW — OpenWakeWord)

| Property | Value |
|---|---|
| **File** | `models/jarvis_ptbr_user.onnx` |
| **Size** | 858,869 bytes (838 KB) |
| **SHA256** | `b6e86a78e3b9aa5d3709e3f938938345dc151914f009a93b1b6715d66a99117b` |
| **Label** | `jarvis_ptbr_user` |
| **Type** | PT-BR custom trained (Will's voice) |
| **Provider** | `CUDAExecutionProvider` |
| **Threshold** | 0.5 (recomendado) |
| **Candidate threshold** | 0.35 |
| **Confirm min RMS** | 50 |

### Verificação

```bash
sha256sum models/jarvis_ptbr_user.onnx
# esperado: b6e86a78e3b9aa5d3709e3f938938345dc151914f009a93b1b6715d66a99117b
```

## 2. TTS Voice Model (OmniVoice — jarvis-clone-trimmed)

| Property | Value |
|---|---|
| **WAV file** | `models/jarvis-clone-trimmed.wav` |
| **Size** | 528,076 bytes (515 KB) |
| **SHA256** | `49ef07da5274a14454cccdc497f335f00200c1f5b32cbdf786411bc9ab207142` |
| **Ref text** | `models/jarvis-clone-trimmed.txt` (180 bytes) |
| **Training data** | `models/voice-instance/ref_texts/jarvis-clone.txt` |
| **Endpoint** | `http://127.0.0.1:8202/v1/audio/speech` |
| **Voice ID** | `jarvis-clone-trimmed` |
| **Synthesis** | Sub-sentence streaming (8-15 words) |
| **First chunk latency** | <500ms |

### Verificação

```bash
sha256sum models/jarvis-clone-trimmed.wav
# esperado: 49ef07da5274a14454cccdc497f335f00200c1f5b32cbdf786411bc9ab207142
```

## Como usar

```python
import openwakeword
from openwakeword.model import Model

# Wake
model = Model(
    wakeword_models=["models/jarvis_ptbr_user.onnx"],
    inference_framework="onnx",
)
predictions = model.predict(audio_chunk)
if predictions["jarvis_ptbr_user"] > 0.5:
    print("Wake detected!")
```

## Como treinar (custom voice)

```bash
# 1. Gravar 5 min de audio (WAV, 16kHz, mono)
# 2. Treinar
python -m openwakeword.train \
  --audio samples/wake_jarvis_5min.wav \
  --label jarvis_ptbr_user \
  --output models/jarvis_ptbr_user.onnx
```

## License

MIT (modelos são do Will, podem ser usados livremente).
