"""JarvisVoiceClonePlugin: hermes-jarvis-voice-clone para hermes-agent."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("hermes-jarvis-voice-clone")


class JarvisVoiceClonePlugin:
    """Plugin data."""
    name = "hermes-jarvis-voice-clone"
    kind = "data"
    version = "1.0.0"

    def register(self, ctx) -> None:
        """Hook de registro."""
        # Tools
        ctx.register_tool("hermes_jarvis_voice_clone_status", self._tool_status)

        # Skills
        skill_path = self._skill_path()
        if skill_path.exists():
            ctx.register_skill("hermes-jarvis-voice-clone", skill_path)

        log.info("hermes-jarvis-voice-clone v%s registrado", self.version)

    def _skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "skills" / "jarvis-voice-clone"

    def _tool_status(self, **_):
        return {"status": "ready", "version": self.version}
