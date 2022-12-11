import random
from typing import List

import torch
from parlai.core.script import ParlaiPreloadModelScript

import schema


class KnowledgeGroundingService:
    def __init__(self, init_model_path: str, model_path: str):
        random.seed(42)

        self.cuda_device = self._init_device()

        self._kg_script = ParlaiPreloadModelScript.main(
            task="topical_chat:generator",
            init_model=init_model_path,
            model_file=model_path,
            fp16=False,
            inference="nucleus",
            topp=0.9,
            skip_generation=False,
        )

    def perform(self, input: List[schema.RequestSample]) -> List[str]:
        ks_script_input = _convert_to_kg_script_input(input)
        raw_responses = self._kg_script.run(ks_script_input.dict())
        
        return [r["text"] for r in raw_responses]

    def _init_device(self) -> str:
        cuda = torch.cuda.is_available()

        if cuda:
            torch.cuda.set_device(0)  # singe gpu
            return torch.device("cuda")
        
        return torch.device("cpu")


def _convert_to_kg_script_input(input: List[schema.RequestSample]) -> schema.KgModelInput:
    history = input[0].history.split("\n") if input[0].history else [""]
    kg_input = schema.KgModelInput(history=history, inputs=[])

    for sample in input:
        kg_input.inputs.append(schema.Sample(
            checked_sentence=sample.checked_sentence,
            knowledge=sample.knowledge,
            text=sample.text
        ))
    
    return kg_input

