import comfy.samplers
import os
import yaml

base_path = os.path.dirname(os.path.realpath(__file__))
models_subdir = "../../models"
configs_subdir = "configs/checkpoints"

# Get the directory paths
models_dir = os.path.join(base_path, models_subdir)
config_file_directory = os.path.join(models_dir, configs_subdir)

config_files = [f for f in os.listdir(config_file_directory) if os.path.isfile(os.path.join(config_file_directory, f))]

# This node allows loading configuration per checkpoint.
class CheckpointLoaderConfigCustomNode:
    CATEGORY = "utils"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "config_file": (config_files,),
        }}
    RETURN_TYPES = (
                    "FLOAT",
                    "INT",
                    comfy.samplers.KSampler.SAMPLERS,
                    comfy.samplers.KSampler.SCHEDULERS,
                    "INT",
                    "FLOAT"
                    )
    RETURN_NAMES = (
                    "cfg",
                    "steps",
                    "sampler",
                    "scheduler",
                    "seed",
                    "denoise"
    )
    FUNCTION = "load_checkpoint_configuration"

    # Load a config from the models/configs directory based on the checkpoint name.
    def load_checkpoint_configuration(self, config_file):
        config_file = os.path.join(config_file_directory, config_file)
        if not os.path.exists(config_file):
            raise ValueError(f"Config  not found. Expected path: {config_file}")

        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            cfg = config.get('cfg', 4)
            steps = config.get('steps', 10)
            sampler_name = config.get('sampler', "euler")
            scheduler_name = config.get('scheduler', "normal")
            seed = config.get('seed', -1)
            denoise = config.get('denoise', 1.0)

        loaded_config = (
            cfg,
            steps,
            sampler_name,
            scheduler_name,
            seed,
            denoise
        )
        print(f"Loaded config: {loaded_config}")
        return loaded_config
