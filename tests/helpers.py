import json
from typing import Type, Sequence
from pathlib import Path

import torch

from zkstats.core import prover_gen_settings, verifier_setup, prover_gen_proof, verifier_verify, get_data_commitment_maps
from zkstats.computation import IModel, IsResultPrecise


def compute(basepath: Path, data: list[torch.Tensor], model: Type[IModel], scales: Sequence[int]) -> IsResultPrecise:
    sel_data_path = basepath / "comb_data.json"
    model_path = basepath / "model.onnx"
    settings_path = basepath / "settings.json"
    witness_path = basepath / "witness.json"
    compiled_model_path = basepath / "model.compiled"
    proof_path = basepath / "model.proof"
    pk_path = basepath / "model.pk"
    vk_path = basepath / "model.vk"
    data_path = basepath / "data.json"

    column_names = [f"columns_{i}" for i in range(len(data))]
    column_to_data = {
        column: d.tolist()
        for column, d in zip(column_names, data)
    }
    with open(data_path, "w") as f:
        json.dump(column_to_data, f)

    commitment_maps = get_data_commitment_maps(data_path, scales)

    prover_gen_settings(
        data_path=data_path,
        col_array=list(column_to_data.keys()),
        sel_data_path=str(sel_data_path),
        prover_model=model,
        prover_model_path=str(model_path),
        scale=scales,
        mode="resources",
        settings_path=str(settings_path),
    )
    verifier_setup(
        str(model_path),
        str(compiled_model_path),
        str(settings_path),
        str(vk_path),
        str(pk_path),
    )
    prover_gen_proof(
        str(model_path),
        str(sel_data_path),
        str(witness_path),
        str(compiled_model_path),
        str(settings_path),
        str(proof_path),
        str(pk_path),
    )
    verifier_verify(
        str(proof_path),
        str(settings_path),
        str(vk_path),
        column_names,
        commitment_maps,
    )
