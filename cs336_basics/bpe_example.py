from Regex import re

exampleText = "low low low low low lower lower widest widest widest newest newest newest newest newest newest"


def pretokenize(text: str) -> list[str]:
    return list(text)


def merge_bpe(pretokens: list[str], initial_vocab: dict[int, bytes]) -> dict[int, bytes]:
    pass


def build_vocab(text: str) -> dict[int, bytes]:
    initial_vocab: dict[int, bytes] = {k: bytes([k]) for k in range(256)}
    pretokens = pretokenize(text)
    vocab = merge_bpe(pretokens, initial_vocab)
    return vocab


def bpe_tokenizer(text: str) -> list[int]:
    pass
