from mnemonic import Mnemonic


def generate_seed_phrase(word_count, language):
    strength = {12: 128, 15: 160, 18: 192,
                21: 224, 24: 256}.get(word_count, 128)
    mnemo = Mnemonic(language)
    return mnemo.generate(strength)