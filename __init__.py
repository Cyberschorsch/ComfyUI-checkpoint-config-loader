from .CheckpointLoaderConfigCustomNode import CheckpointLoaderConfigCustomNode

NODE_CLASS_MAPPINGS = { "Checkpoint Loader Config" : CheckpointLoaderConfigCustomNode }

def load_node(node_name):
    return NODE_CLASS_MAPPINGS.get(node_name)

__all__ = ["load_node"]