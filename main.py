import sys
sys.path.append('src/deepvoice3-pytorch')


def load_model(model_name):
    from train import build_model
    from train import restore_parts, load_checkpoint

    checkpoint_path = model_name
    model = build_model()
    model = load_checkpoint(checkpoint_path, model, None, True)
    return model


def import_config(config):
    import hparams
    import json

    # Load parameters from preset
    with open(config) as f:
      hparams.hparams.parse_json(f.read())

    # Inject frontend text processor
    import synthesis
    import train
    from deepvoice3_pytorch import frontend
    synthesis._frontend = getattr(frontend, "en")
    train._frontend = getattr(frontend, "en")
    # hparams.hparams.sample_rate = 48000
    hparams.hparams.fmax=20000


def tts(model, text, file_path, p=0, speaker_id=None, fast=True):
    from synthesis import tts as _tts
    import audio

    waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)

    # 22050, 353 kbps, 16 bit, mono
    audio.save_wav(waveform, file_path)


if __name__ == "__main__":
    args = sys.argv
    model_name = args[1]
    config = args[2]
    text = args[3]
    file_name = args[4]

    import_config(config)
    model = load_model(model_name)
    tts(model, text, file_name)
