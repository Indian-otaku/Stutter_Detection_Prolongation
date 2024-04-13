import os
import pathlib

class Config:

    CWD : str = os.getcwd()
    AUDIO_FOLDER_WD : str = os.path.join(CWD, pathlib.Path("AudioFolder"))
    SAVED_CHECKPOINT_PATH = os.path.join(CWD, "utils", "saved_model", "checkpoint_prolongation.pth")
    SAVED_W2V2_PATH = os.path.join(CWD, "utils", "saved_model", "w2v2_architecture")

    SAMPLE_RATE = 16000

if __name__ == "__main__":
    print(Config.CWD)
    print(Config.AUDIO_FOLDER_WD, os.path.exists(Config.AUDIO_FOLDER_WD))
    print(Config.SAVED_CHECKPOINT_PATH, os.path.exists(Config.SAVED_CHECKPOINT_PATH))
    print(Config.SAVED_W2V2_PATH, os.path.exists(Config.SAVED_W2V2_PATH))