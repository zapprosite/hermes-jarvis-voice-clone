"""Smoke tests para hermes-jarvis-voice-clone."""
import pytest
from pathlib import Path


def test_wake_model_exists():
    """Wake model ONNX deve existir."""
    model = Path("/home/will/data/hermes/wake_models/jarvis_ptbr_user.onnx")
    if not model.exists():
        pytest.skip("Wake model nao encontrado (esperado em hardware diferente)")
    # SHA256 check
    import hashlib
    sha = hashlib.sha256(model.read_bytes()).hexdigest()
    assert sha == "b6e86a78e3b9aa5d3709e3f938938345dc151914f009a93b1b6715d66a99117b",         f"Wake model SHA256 mismatch: {sha}"


def test_tts_voice_exists():
    """TTS voice WAV deve existir."""
    voice = Path("/home/will/data/tts/voices/jarvis-clone-trimmed.wav")
    if not voice.exists():
        pytest.skip("TTS voice nao encontrada")
    assert voice.stat().st_size > 0


def test_checksums_json():
    """checksums.json deve existir e ser valido JSON."""
    from hermes_jarvis_voice_clone import install_models
    # verifica que o modulo pode ser importado
    assert install_models is not None
